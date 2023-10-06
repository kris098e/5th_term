
# This module takes the intermediate code and outputs 64 bit x86 assembler.


from code_generation import Op, T, M, Meta, Labels

# The code generation strategy does not use registers for storing values
# over function calls. All longer term values are on the stack. Thus,
# the caller/calle save protocols are not required. They are available
# in case we decide to implement optimizations and change the code.

_full_caller_callee_save = False


# The number of caller-save registers are relevant since computed values
# for function calls must be obtained from below the caller-saved
# registers to be pushed on the stack (in reverse order).

if _full_caller_callee_save:
    _caller_registers = 8
else:
    _caller_registers = 0


_intermediate_to_x86 = {
    Op.MOVE: "movq",
    Op.CALL: "callq",
    Op.PUSH: "pushq",
    Op.POP: "popq",
    Op.CMP: "cmpq",
    Op.JMP: "jmp",
    Op.JE: "je",
    Op.JNE: "jne",
    Op.JL: "jl",
    Op.JLE: "jle",
    Op.JG: "jg",
    Op.JGE: "jge",
    Op.ADD: "addq",
    Op.SUB: "subq",
    Op.MUL: "imulq",
    }


# Emitting


class Emit:
    """The class that emits 64 bit x86 assembler code. Attempts are made
       to make the code human readable.
    """
    def __init__(self, intermediate_representation, macOS):
        self.intermediate_representation = intermediate_representation
        # The unique labels generator:
        self._labels = Labels()
        self.macOS = macOS
        self.instruction_indent = 16
        self.instruction_width = 24
        self.max_width = 79
        self.code = []

    def emit(self):
        self.program_prologue()
        for instruction in self.intermediate_representation:
            self._dispatch(instruction)
        self.program_epilogue()

    def get_code(self):
        self.code.append("\n")
        return "\n".join(self.code)

    def _format_comment(self, comment):
        """Formats comments that would make the total line length too large
           by using multiple lines.
        """
        width = self.max_width-self.instruction_indent-self.instruction_width-2
        page = []
        line = ""
        for word in comment.split():
            if not line:
                line += word
            else:
                if len(line) + 1 + len(word) <= width:
                    line += " " + word
                else:
                    page.append(line)
                    line = word
        if line:
            page.append(line)
        delimiter = "\n" + (self.max_width - width - 2) * " " + "# "
        return delimiter.join(page)

    # The following three methods append to self.code:

    def _lbl(self, lbl):
        self.code.append(lbl + ":")

    def _ins(self, instr_str, comment):
        line = self.instruction_indent * " " \
               + instr_str.ljust(self.instruction_width) \
               + "# " + self._format_comment(comment)
        self.code.append(line)

    def _raw(self, s):
        self.code.append(s)

    # Emitting intermediate representation instructions:

    def _dispatch(self, instr):
        if instr.opcode in _intermediate_to_x86:
            self._simple_instruction(instr)
        else:
            match instr.opcode:
                case Op.DIV:
                    self._div(instr)
                case Op.RET:
                    self._ret(instr)
                case Op.LABEL:
                    self._label(instr)
                case Op.META:
                    method = instr.args[0]
                    match method:
                        case Meta.PROGRAM_PROLOGUE:
                            self.program_prologue()
                        case Meta.PROGRAM_EPILOGUE:
                            self.program_epilogue()
                        case Meta.MAIN_CALLEE_SAVE:
                            self.main_callee_save()
                        case Meta.MAIN_CALLEE_RESTORE:
                            self.main_callee_restore()
                        case Meta.CALLEE_PROLOGUE:
                            self.callee_prologue()
                        case Meta.CALLEE_EPILOGUE:
                            self.callee_epilogue()
                        case Meta.CALLEE_SAVE:
                            self.callee_save()
                        case Meta.CALLEE_RESTORE:
                            self.callee_restore()
                        case Meta.CALLER_PROLOGUE:
                            self.caller_prologue()
                        case Meta.CALLER_EPILOGUE:
                            self.caller_epilogue()
                        case Meta.CALLER_SAVE:
                            self.caller_save()
                        case Meta.CALLER_RESTORE:
                            self.caller_restore()
                        case Meta.POP_EXPRESSION_RESULT:
                            self.pop_expression_result()
                        case Meta.CALL_PRINTF:
                            self.call_printf()
                        case Meta.ALLOCATE_STACK_SPACE:
                            self.allocate_stack_space(instr.args[1])
                        case Meta.DEALLOCATE_STACK_SPACE:
                            self.deallocate_stack_space(instr.args[1])
                        case Meta.REVERSE_PUSH_ARGUMENTS:
                            self.reverse_push_arguments(instr.args[1])

    def _do_arg(self, arg):
        """Formats one instruction argument."""
        target = arg.target
        match target.spec:
            case T.IMI | T.IML:
                text = f"${target.val}"
            case T.MEM:
                text = f"{target.val}"
            case T.RBP:
                text = "%rbp"
            case T.RSP:
                text = "%rsp"
            case T.RRT:
                text = "%rax"
            case T.RSL:
                text = "%rdx"
            case T.REG:
                match target.val:
                    case 1:
                        text = "%rbx"
                    case 2:
                        text = "%rcx"
        addressing = arg.addressing
        match addressing.mode:
            case M.DIR:
                pass
            case M.IND:
                text = f"({text})"
            case M.IRL:
                text = f"{-8*addressing.offset}({text})"
        return text

    def _simple_instruction(self, instr):
        """Most instructions simply have their opcode translated to the
           64 bit x86 syntax and their one or two parameters formated by
           _do_arg. This method implements this generically.
        """
        line = _intermediate_to_x86[instr.opcode]
        if len(instr.args) > 0:
            line += " " + self._do_arg(instr.args[0])
        for i in range(1, len(instr.args)):
            line += ", " + self._do_arg(instr.args[i])
        self._ins(line, instr.comment)

    # The few instruction that do not follow the simple pattern:

    def _div(self, instr):
        self._ins(f"movq {self._do_arg(instr.args[1])}, %rax",
                  "prepare for division")
        self._ins("cqo", "sign extend")
        self._ins(f"idivq {self._do_arg(instr.args[0])}", "divide")
        self._ins(f"movq %rax, {self._do_arg(instr.args[1])}",
                  "move to destination")

    def _label(self, instr):
        s = ""
        if self.macOS and instr.args[0].target.val == 'main':
            s = "_"
        self._lbl(s + self._do_arg(instr.args[0]))

    def _ret(self, instr):
        self._ins("popq %rax", "move return value to return register")
        self._ins(f"jmp {instr.args[0]}", "jump to function epiloque")

    # Block code for prologues, epilogues, printing, etc.:

    def program_prologue(self):
        self._raw("")
        self._raw(".data")
        self._raw("")
        self._lbl("form")
        self._ins('.string "%d\\n"', "form string for C printf")
        self._raw("")
        self._raw(".text")
        self._raw("")
        self._raw(f".globl {'_' if self.macOS else ''}main")
        self._raw("")

    def program_epilogue(self):
        pass

    def main_callee_save(self):
        self._raw("")
        self._ins("pushq %rbx", "%rbx is callee save")
        self._ins("pushq %r12", "%r12 is callee save")
        self._ins("pushq %r13", "%r13 is callee save")
        self._ins("pushq %r14", "%r14 is callee save")
        self._ins("pushq %r15", "%r15 is callee save")
        self._raw("")

    def callee_save(self):
        if _full_caller_callee_save:
            self.main_callee_save()

    def main_callee_restore(self):
        self._raw("")
        self._ins("popq %r15", "restore callee save register")
        self._ins("popq %r14", "restore callee save register")
        self._ins("popq %r13", "restore callee save register")
        self._ins("popq %r12", "restore callee save register")
        self._ins("popq %rbx", "restore callee save register")
        self._raw("")

    def callee_restore(self):
        if _full_caller_callee_save:
            self.main_callee_restore()

    def callee_prologue(self):
        self._raw("")
        self._ins("", "CALLEE PROLOGUE")
        self._ins("pushq %rbp", "save caller's base pointer")
        self._ins("movq %rsp, %rbp", "make stack pointer new base pointer")
        self._raw("")

    def callee_epilogue(self):
        self._raw("")
        self._ins("", "CALLEE EPILOGUE")
        self._ins("movq %rbp, %rsp", "restore stack pointer")
        self._ins("popq %rbp", "restore base pointer")
        self._ins("ret", "return from call")
        self._raw("")

    def caller_save(self):
        if _full_caller_callee_save:
            self._raw("")
            self._ins("pushq %rcx", "%rcx is caller save")
            self._ins("pushq %rdx", "%rdx is caller save")
            self._ins("pushq %rsi", "%rsi is caller save")
            self._ins("pushq %rdi", "%rdi is caller save")
            self._ins("pushq %r8", "%r8 is caller save")
            self._ins("pushq %r9", "%r9 is caller save")
            self._ins("pushq %r10", "%r10 is caller save")
            self._ins("pushq %r11", "%r11 is caller save")
            self._raw("")

    def caller_restore(self):
        if _full_caller_callee_save:
            self._raw("")
            self._ins("popq %r11", "restore caller save register")
            self._ins("popq %r10", "restore caller save register")
            self._ins("popq %r9", "restore caller save register")
            self._ins("popq %r8", "restore caller save register")
            self._ins("popq %rdi", "restore caller save register")
            self._ins("popq %rsi", "restore caller save register")
            self._ins("popq %rdx", "restore caller save register")
            self._ins("popq %rcx", "restore caller save register")
            self._raw("")

    def pop_expression_result(self):
        self._ins("addq $8, %rsp", "pop expression from stack")
        self._raw("")

    def caller_prologue(self):
        self._ins("", "CALLER PROLOGUE: empty")
        self._raw("")

    def caller_epilogue(self):
        self._ins("", "CALLER EPILOGUE: empty")
        self._raw("")

    def call_printf(self):
        self._ins("", "PRINTING")
        self._ins("leaq form(%rip), %rdi", "pass 1. argument in %rdi")
        # By-passing caller save values on the stack:
        self._ins(f"movq {8*_caller_registers}(%rsp), %rsi",
                  "pass 2. argument in %rsi")
        self._ins("movq $0, %rax", "no floating point registers used")
        self._ins("testq $15, %rsp", "test for 16 byte alignment")
        lbl = self._labels.next("aligned")
        self._ins(f"jz {lbl}", "jump if aligned")
        self._ins("addq $-8, %rsp", "16 byte aligning")
        self._ins(f"callq {'_printf' if self.macOS else 'printf@plt'}",
                  "call printf")
        self._ins("addq $8, %rsp", "reverting alignment")
        lbl_end = self._labels.next("end_aligned")
        self._ins(f"jmp {lbl_end}", "")
        self._raw(f"{lbl}:")
        self._ins(f"callq {'_printf' if self.macOS else 'printf@plt'}",
                  "call printf")
        self._raw(f"{lbl_end}:")
        self._raw("")

    def allocate_stack_space(self, words):
        self._ins(f"addq ${-8*words}, %rsp",
                  "allocate space for local variables")
        self._raw("")

    def deallocate_stack_space(self, words):
        self._ins(f"addq ${8*words}, %rsp",
                  "deallocate stack space for parameters or local variables")
        self._raw("")

    def reverse_push_arguments(self, number_of_arguments):
        """By-passing the caller-saved values on the stack, moving down
           in the stack for the next actual parameter, remembering that
           the stack grows for each push.
        """
        for i in range(number_of_arguments):
            offset = 8 * (_caller_registers + 2 * i)
            self._ins(f"pushq {offset}(%rsp)",
                      "push arguments in reverse order")
