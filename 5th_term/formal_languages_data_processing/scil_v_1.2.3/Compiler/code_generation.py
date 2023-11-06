
# This module performs the compilation from an abstract syntax tree to
# an intermediate representation close to linear 64 bit x86 code. See the
# documentation for a definition of the intermediate representation.
# It is based on the visitors_base and AST modules that together implement
# the recursive traversal and visit functionality.


from enum import Enum, auto
from singleton_decorator import singleton
from visitors_base import VisitorsBase
from symbols import NameCategory

# autogenerating enumuration types for the intermediate representation:
class Op(Enum):
    """Defines the various operations."""
    MOVE = auto()
    PUSH = auto()
    POP = auto()
    CALL = auto()
    RET = auto()
    CMP = auto()
    JMP = auto()
    JE = auto()
    JNE = auto()
    JL = auto()
    JLE = auto()
    JG = auto()
    JGE = auto()
    ADD = auto()
    SUB = auto()
    MUL = auto()
    DIV = auto()
    LABEL = auto()
    META = auto()


class T(Enum):
    """Defines an enumeration type for instruction argument targets. """
    IMI = auto()  # immediate integer
    IML = auto()  # immediate label
    MEM = auto()  # memory (a label)
    RBP = auto()  # register: base (frame) pointer
    RSP = auto()  # register: stack pointer
    RRT = auto()  # register: return value
    RSL = auto()  # register: static link computation
    REG = auto()  # general-purpose registers


class M(Enum):
    """Defines an enumeration type for addressing modes. """
    DIR = auto()  # direct
    IND = auto()  # indirect
    IRL = auto()  # indirect relative


class Target:
    """Specification of a target, using class T, and an optional argument."""
    def __init__(self, spec, *args):
        self.spec = spec
        if args:
            self.val = args[0]


class Mode:
    """Specification of an addressing mode, using class M, and an optional
       argument.
    """
    def __init__(self, mode, *args):
        self.mode = mode
        if args:
            self.offset = args[0]

# Instruction arguments representation:
class Arg:
    """Representation of instruction arguments with a target and a mode."""
    def __init__(self, target, addressing):
        self.target = target
        self.addressing = addressing

# Instruction representation:
class Ins:
    """Representation of an instruction with an opcode, a number of
       arguments, and an optional comment.
    """
    def __init__(self, *args, c=""):
        self.opcode = args[0]
        self.args = args[1:]
        self.comment = c


class Meta(Enum):
    PROGRAM_PROLOGUE = auto()
    PROGRAM_EPILOGUE = auto()
    MAIN_CALLEE_SAVE = auto()
    MAIN_CALLEE_RESTORE = auto()
    CALLEE_PROLOGUE = auto()
    CALLEE_EPILOGUE = auto()
    CALLEE_SAVE = auto()
    CALLEE_RESTORE = auto()
    CALLER_PROLOGUE = auto()
    CALLER_EPILOGUE = auto()
    CALLER_SAVE = auto()
    CALLER_RESTORE = auto()
    POP_EXPRESSION_RESULT = auto()
    CALL_PRINTF = auto()
    ALLOCATE_STACK_SPACE = auto()
    DEALLOCATE_STACK_SPACE = auto()
    REVERSE_PUSH_ARGUMENTS = auto()


@singleton
class Labels:
    """Generate unique labels with a descriptive string at the end.
    Labels and used in code generation as well as emit, and uniqueness of
    labels across the modules is ensured via the singleton decorator.
    """
    def __init__(self):
        self.counter = -1

    def next(self, s):
        self.counter += 1
        return "F" + str(self.counter).zfill(4) + "_" + s


# Code Generation

class ASTCodeGenerationVisitor(VisitorsBase):
    """Implements the intermediate code generation from the AST."""
    def __init__(self):
        # The current scope in the form of a reference to the local
        # symbol table, from where parent scopes can be reached:
        self._current_scope = None
        # A stack of references to the definitions of functions in the
        # AST, representing the current nesting of scopes:
        self._function_stack = []
        # The unique labels generator:
        self._labels = Labels()
        # The code is collected in a list:
        self._code = []

    def get_code(self):
        return self._code

    def _app(self, instruction):
        self._code.append(instruction)

    def _follow_static_link(self, level_difference):
        """Generates code to follow static link; at the end, rsl will
           point to rbp in the correct frame.
        """
        self._app(Ins(Op.MOVE,
                      Arg(Target(T.RBP), Mode(M.DIR)),
                      Arg(Target(T.RSL), Mode(M.DIR)),
                      c="preparing for static link computation"))
        for i in range(level_difference):
            # Static link is offset two from base pointer: look at the slides for code generation to see why
            self._app(Ins(Op.MOVE,
                          Arg(Target(T.RSL), Mode(M.IRL, -2)),
                          Arg(Target(T.RSL), Mode(M.DIR)),
                          c="following the static link"))

    def _ensure_labels(self, t):
        if not hasattr(t, 'start_label'):
            t.start_label = self._labels.next(t.name)
            t.end_label = self._labels.next(f"end_{t.name}")

    def postMidVisit_body(self, t):
        self._ensure_labels(self._function_stack[-1]) # make sure label is there
        label = self._function_stack[-1].start_label
        self._app(Ins(Op.LABEL, Arg(Target(T.MEM, label), Mode(M.DIR))))
        self._app(Ins(Op.META, Meta.CALLEE_PROLOGUE)) # do the callee prologue when emitting
        self._app(Ins(Op.META,
                      Meta.ALLOCATE_STACK_SPACE,
                      t.number_of_variables))
        if len(self._function_stack) == 1:
            # In the body of main:
            self._app(Ins(Op.META, Meta.MAIN_CALLEE_SAVE))
        else:
            # In the body of a function:
            self._app(Ins(Op.META, Meta.CALLEE_SAVE))

    def postVisit_body(self, t):
        lbl = self._function_stack[-1].end_label
        self._app(Ins(Op.LABEL, Arg(Target(T.MEM, lbl), Mode(M.DIR))))
        if len(self._function_stack) == 1:
            # In the body of main:
            self._app(Ins(Op.META, Meta.MAIN_CALLEE_RESTORE))
        else:
            # In the body of a function:
            self._app(Ins(Op.META, Meta.CALLEE_RESTORE))
        self._app(Ins(Op.META, Meta.CALLEE_EPILOGUE))

    def preVisit_function(self, t):
        self._current_scope = t.symbol_table
        self._function_stack.append(t)
        if t.name == "main":
            t.start_label = "main"
            t.end_label = "end_main"

    def postVisit_function(self, t):
        self._function_stack.pop()
        self._current_scope = self._current_scope.parent

    def postVisit_statement_return(self, t):
        # Getting the function label from the nearest enclosing function:
        label = self._function_stack[-1].end_label
        self._app(Ins(Op.RET, label))

    def postVisit_statement_print(self, t):
        self._app(Ins(Op.META, Meta.CALLER_SAVE))
        self._app(Ins(Op.META, Meta.CALLER_PROLOGUE))
        self._app(Ins(Op.META, Meta.CALL_PRINTF))
        self._app(Ins(Op.META, Meta.CALLER_EPILOGUE))
        self._app(Ins(Op.META, Meta.CALLER_RESTORE))
        self._app(Ins(Op.META, Meta.POP_EXPRESSION_RESULT))

    def postVisit_statement_assignment(self, t):
        """                move rbp, rsl
                           move -2(rsl), rsl  # number of level diff times
                           pop some_offset(rsl)
        """
        value = self._current_scope.lookup(t.lhs)
        # Follow static link:
        level_difference = self._function_stack[-1].scope_level - value.level
        self._follow_static_link(level_difference)
        # The left-hand side must be a local variable in some scope:
        offset = value.info
        self._app(Ins(Op.POP,
                      Arg(Target(T.RSL), Mode(M.IRL, 1 + offset)),
                      c="assigning the computed expression"))

    def preVisit_statement_ifthenelse(self, t):
        t.else_label = self._labels.next("else")
        t.endif_label = self._labels.next("endif")

    def preMidVisit_statement_ifthenelse(self, t):
        """                pop reg1
                           move false, reg2
                           cmp reg1, reg2
                           je else_label
        """
        self._app(Ins(Op.POP,
                      Arg(Target(T.REG, 1), Mode(M.DIR)),
                      c="move computed boolean to register"))
        self._app(Ins(Op.MOVE,
                      Arg(Target(T.IMI, 0), Mode(M.DIR)),
                      Arg(Target(T.REG, 2), Mode(M.DIR)),
                      c="move false to register"))
        self._app(Ins(Op.CMP,
                      Arg(Target(T.REG, 1), Mode(M.DIR)),
                      Arg(Target(T.REG, 2), Mode(M.DIR)),
                      c="compare computed boolean to false"))
        self._app(Ins(Op.JE,
                      Arg(Target(T.MEM, t.else_label), Mode(M.DIR)),
                      c="jump to else-part if false"))

    def postMidVisit_statement_ifthenelse(self, t):
        """                jmp endif_label
           else_label:
        """
        self._app(Ins(Op.JMP, Arg(Target(T.MEM, t.endif_label), Mode(M.DIR))))
        self._app(Ins(Op.LABEL, Arg(Target(T.MEM, t.else_label), Mode(M.DIR))))

    def postVisit_statement_ifthenelse(self, t):
        """endif_label:
        """
        self._app(Ins(Op.LABEL,
                      Arg(Target(T.MEM, t.endif_label), Mode(M.DIR))))

    def preVisit_statement_repeat_until(self, t):
        """repeat_label:
        """
        t.repeat_label = self._labels.next("repeat")
        t.endrepeat_label = self._labels.next("endrepeat")
        self._app(Ins(Op.LABEL,
                      Arg(Target(T.MEM, t.repeat_label), Mode(M.DIR))))
        
    def preVisit_statement_while(self, t):
        """while_label:
        """
        t.while_label = self._labels.next("while") # assembly label for the while, put a unique label on it. Add a number to the end.
        t.endwhile_label = self._labels.next("endwhile") # assembly label for the end of the while, put a unique label on it. Add a number to the end.
        self._app(Ins(Op.LABEL,
                      Arg(Target(T.MEM, t.while_label), Mode(M.DIR)))) 
        # app: append to the list of instructions, Op: operation, LABEL: label, Arg: argument, Target: target, T.MEM: memory, t.while_label: the label, Mode: mode, M.DIR: direct addressing mode

    def midVisit_statement_repeat_until(self, t):
        """                pop reg1
                           move false, reg2
                           cmp reg1, reg2
                           jne repeat_label
                           endrepeat_label
        """
        self._app(Ins(Op.POP,
                      Arg(Target(T.REG, 1), Mode(M.DIR)),
                      c="move computed boolean to register"))
        self._app(Ins(Op.MOVE,
                      Arg(Target(T.IMI, 0), Mode(M.DIR)),
                      Arg(Target(T.REG, 2), Mode(M.DIR)),
                      c="move false to register"))
        self._app(Ins(Op.CMP,
                      Arg(Target(T.REG, 1), Mode(M.DIR)),
                      Arg(Target(T.REG, 2), Mode(M.DIR)),
                      c="compare computed boolean to false"))
        self._app(Ins(Op.JNE,
                      Arg(Target(T.MEM, t.repeat_label), Mode(M.DIR)),
                      c="jump to repeat if false"))
        self._app(Ins(Op.LABEL,
                      Arg(Target(T.MEM, t.endrepeat_label), Mode(M.DIR))))
        
        
    def midVisit_statement_while(self, t):
        """                pop reg1
                           move false, reg2
                           cmp reg1, reg2
                           je endwhile_label
        """
        # app: append to the list of instructions, Op: operation, POP: pop, Arg: argument, Target: target, T.REG: register, 1: register 1, Mode: mode, M.DIR: direct addressing mode
        self._app(Ins(Op.POP,
                      Arg(Target(T.REG, 1), Mode(M.DIR)),
                      c="move computed boolean to register"))
        # app: append to the list of instructions, Op: operation, MOVE: move, Arg: argument, Target: target, T.IMI: immediate integer, 0: 0, Mode: mode, M.DIR: direct addressing mode
        self._app(Ins(Op.MOVE,
                      Arg(Target(T.IMI, 0), Mode(M.DIR)),
                      Arg(Target(T.REG, 2), Mode(M.DIR)),
                      c="move false to register"))
        # Compare instruction, between register 1 and register 2
        self._app(Ins(Op.CMP,
                      Arg(Target(T.REG, 1), Mode(M.DIR)),
                      Arg(Target(T.REG, 2), Mode(M.DIR)),
                      c="compare computed boolean to false"))
        # Jump instruction, if equal, jump to end while
        self._app(Ins(Op.JE,
                      Arg(Target(T.MEM, t.endwhile_label), Mode(M.DIR)),
                      c="jump to end_while if false"))

    def postVisit_statement_while(self, t):
        """                jmp while_label
           endwhile_label:
        """
        # Jump instruction, jump to the while label
        self._app(Ins(Op.JMP, Arg(Target(T.MEM, t.while_label), Mode(M.DIR))))
        # Label instruction, label the end of the while
        self._app(Ins(Op.LABEL,
                      Arg(Target(T.MEM, t.endwhile_label), Mode(M.DIR))))

    def postVisit_expression_integer(self, t):
        """                push int
        """
        self._app(Ins(Op.PUSH,
                      Arg(Target(T.IMI, t.integer), Mode(M.DIR)),
                      c="push integer expression"))

    def postVisit_expression_identifier(self, t):
        """                move rbp, rsl
                           move -2(rsl), rsl  # number of level diff times
                           push some_offset(rsl)
        """
        value = self._current_scope.lookup(t.identifier)
        # Follow static link:
        level_difference = self._function_stack[-1].scope_level - value.level # find the level difference between the current scope and the scope of the identifier
        self._follow_static_link(level_difference) # follow the static link, if not in the same scope. 
        if value.cat == NameCategory.PARAMETER: # if the value is a parameter, have to find the offset onto the stack
            offset = value.info
            self._app(Ins(Op.PUSH,
                          Arg(Target(T.RSL), Mode(M.IRL, -(offset + 3))), # offset is the offset to the parameter, fx first parameter is offset 0, second is offset 1, etc. use offset 3 as the first parameter is 3 away from the base pointer
                          c=f"push value of {offset+1}. parameter"))
        elif value.cat == NameCategory.VARIABLE:
            offset = value.info
            self._app(Ins(Op.PUSH,
                          Arg(Target(T.RSL), Mode(M.IRL, offset + 1)),
                          c=f"push value of {offset+1}. variable"))

    def postVisit_expression_call(self, t):
        """                caller_save
                           caller_prologue
                           reverse_push_arguments
                           set up static link
                           call label
                           remove arguments and static link
                           caller_epilogue
                           caller_restore
                           remove expressions that were used for arguments
                           push rrt
        """
        node = self._current_scope.lookup(t.name).info
        self._app(Ins(Op.META, Meta.CALLER_SAVE))
        self._app(Ins(Op.META, Meta.CALLER_PROLOGUE))
        # Push copies of values up as arguments:
        self._app(Ins(Op.META,
                      Meta.REVERSE_PUSH_ARGUMENTS,
                      node.number_of_parameters))
        # Set up static link:
        level_difference = \
            self._function_stack[-1].scope_level - node.scope_level
        if level_difference == -1:
            # Calling inwards, i.e., a local function:
            self._app(Ins(Op.PUSH, Arg(Target(T.RBP), Mode(M.DIR)),
                      c="set up static link for inner function"))
        else:
            # Calling outwards, i.e., same or outer level:
            self._follow_static_link(level_difference)
            self._app(Ins(Op.PUSH,
                      Arg(Target(T.RSL), Mode(M.IRL, -2)),
                      c="set up static link for outer function"))
        # Call:
        self._ensure_labels(node)
        self._app(Ins(Op.CALL,
                      Arg(Target(T.MEM, node.start_label), Mode(M.DIR))))
        # Deallocate static link and argument copies:
        self._app(Ins(Op.META,
                      Meta.DEALLOCATE_STACK_SPACE,
                      node.number_of_parameters + 1))
        self._app(Ins(Op.META, Meta.CALLER_EPILOGUE))
        self._app(Ins(Op.META, Meta.CALLER_RESTORE))
        # Deallocate the original values computed for actual parameters:
        self._app(Ins(Op.META,
                      Meta.DEALLOCATE_STACK_SPACE,
                      node.number_of_parameters))
        # Push the return value as the result of the call expression:
        self._app(Ins(Op.PUSH,
                      Arg(Target(T.RRT), Mode(M.DIR)),
                      c="push return value as the call result"))

    def _comparison_op(self, trueJump):
        """                pop reg2
                           pop reg1
                           cmp reg2, reg1
                           cond_jump true_label
                           push false
                           jmp end_label
           true_label:
                           push true
           end_label:
        """
        self._app(Ins(Op.POP,
                      Arg(Target(T.REG, 2), Mode(M.DIR)),
                      c="pop 2nd expression to register"))
        self._app(Ins(Op.POP,
                      Arg(Target(T.REG, 1), Mode(M.DIR)),
                      c="pop 1st expression to register"))
        # argument order for conditional jumps is not intuitive:
        self._app(Ins(Op.CMP,
                      Arg(Target(T.REG, 2), Mode(M.DIR)),
                      Arg(Target(T.REG, 1), Mode(M.DIR)),
                      c="compare values"))
        true_label = self._labels.next("cmp_true")
        end_label = self._labels.next("cmp_end")
        self._app(Ins(trueJump,
                      Arg(Target(T.MEM, true_label), Mode(M.DIR)),
                      c="jump if the expression was true"))
        self._app(Ins(Op.PUSH,
                      Arg(Target(T.IMI, 0), Mode(M.DIR)),
                      c="push false"))
        self._app(Ins(Op.JMP,
                      Arg(Target(T.MEM, end_label), Mode(M.DIR)),
                      c="done with comparison"))
        self._app(Ins(Op.LABEL, Arg(Target(T.MEM, true_label), Mode(M.DIR))))
        self._app(Ins(Op.PUSH,
                      Arg(Target(T.IMI, 1), Mode(M.DIR)),
                      c="push true"))
        self._app(Ins(Op.LABEL, Arg(Target(T.MEM, end_label), Mode(M.DIR))))

    def _arithmetic_op(self, op):
        """                pop reg1
                           pop reg2
                           op reg1, reg2
                           push reg2
        """
        self._app(Ins(Op.POP,
                      Arg(Target(T.REG, 1), Mode(M.DIR)),
                      c="pop 2nd expression to register"))
        self._app(Ins(Op.POP,
                      Arg(Target(T.REG, 2), Mode(M.DIR)),
                      c="pop 1st expression to register"))
        self._app(Ins(op,
                      Arg(Target(T.REG, 1), Mode(M.DIR)),
                      Arg(Target(T.REG, 2), Mode(M.DIR)),
                      c="carry out the operation"))
        self._app(Ins(Op.PUSH,
                      Arg(Target(T.REG, 2), Mode(M.DIR)),
                      c="push the resulting value"))

    def postVisit_expression_binop(self, t):
        match t.op:
            case "==":
                self._comparison_op(Op.JE)
            case "!=":
                self._comparison_op(Op.JNE)
            case "<":
                self._comparison_op(Op.JL)
            case "<=":
                self._comparison_op(Op.JLE)
            case ">":
                self._comparison_op(Op.JG)
            case ">=":
                self._comparison_op(Op.JGE)
            case "+":
                self._arithmetic_op(Op.ADD)
            case "-":
                self._arithmetic_op(Op.SUB)
            case "*":
                self._arithmetic_op(Op.MUL)
            case "/":
                self._arithmetic_op(Op.DIV)
