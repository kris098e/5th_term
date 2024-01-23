# Beginning notes
[[lecture_notes_symbol_type_code.pdf]]
- Remember that just doing `{ }` in scil will not introduce a new scope, only a function will.
# Token generation
```python
# define keywords
reserved = {
    'if': 'IF',
    'then': 'THEN',
    'else': 'ELSE',
    'while': 'WHILE',
    'do': 'DO',
    'function': 'FUNCTION',
    'return': 'RETURN',
    'var': 'VAR',
    'print': 'PRINT'
}

# Define the tokens
tokens = (
    'IDENT', 'INT',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'LPAREN', 'RPAREN', 'LCURL', 'RCURL',
    'EQ', 'NEQ', 'LT', 'GT', 'LTE', 'GTE',
    'ASSIGN', 'COMMA', 'SEMICOL',
) + tuple(reserved.values())

# for lexer, regular expression on the right, and what it returns on the left.
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_ASSIGN = r'='
t_COMMA = r','
t_SEMICOL = r';'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LCURL = r'{'
t_RCURL = r'}'
t_EQ = r'=='
t_NEQ = r'!='
t_LT = r'<'
t_GT = r'>'
t_LTE = r'<='
t_GTE = r'>='
```

## with functions
```python
# Find the reserved keyword

# t_IDENT is not just used for identifiers. If the keyword is in the `reserved`-map, then this is the outputted token, else we just assume it is an identifier
def t_IDENT(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'IDENT')    # if reserved keyword, else 'IDENT'
    return t

# Match on numbers, must be an int. Covnert it to python Int.
def t_INT(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        error_message("Lexical Analysis",
                      "Integer value too large.",
                      t.lexer.lineno)
        t.value = 0
    if t.value > int('0x7FFFFFFFFFFFFFFF', 16):
        error_message("Lexical Analysis",
                      "Integer value too large.",
                      t.lexer.lineno)
        t.value = 0
    return t


# Ignored characters
t_ignore = " \t\r|"  # \r included for the sake of windows users


# Important for error handling, that we count for each of the newlines, since they can be on the same line.
def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


# Ignore comments in the compiler.
def t_COMMENT(t):
    r'\#.*'
    pass


def t_error(t):
    error_message("Lexical Analysis",
                  f"Illegal character '{t.value[0]}'.",
                  t.lexer.lineno)
    t.lexer.skip(1)


# Precedence for bison, when to shift or reduce.
precedence = (
    ('right', 'EQ', 'NEQ', 'LT', 'GT', 'LTE', 'GTE'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
)
```

## Precedence
In the provided precedence rules:

```python
precedence = (
    ('right', 'EQ', 'NEQ', 'LT', 'GT', 'LTE', 'GTE'), #Makes sense that these are right associative, as we will want to evealuate the entire right-hand side before assigning something to the identifier or the expression.
    ('left', 'PLUS', 'MINUS'), #makes sense to put this as having lower precedence than TIMES, DIVIDE. As when we have the full expression of E DIVIDE E or E TIMES E we will want to reduce first, before moving on. See [4.2_using_parser_processing]
    ('left', 'TIMES', 'DIVIDE'),
)
```
- `right` means we `shift`
- `left` means we `reduce`

The operators are listed in order of increasing precedence. Therefore, the operators with the highest precedence in this case are `TIMES` (`*`) and `DIVIDE` (`/`). These operators are grouped together and have left associativity, meaning that in an expression, operations involving these operators are evaluated from left to right.

Following these, the operators with the next highest precedence are `PLUS` (`+`) and `MINUS` (`-`), which are also grouped together and have left associativity.

Finally, the operators with the lowest precedence in this list are the comparison operators: `EQ` (`==`), `NEQ` (`!=`), `LT` (`<`), `GT` (`>`), `LTE` (`<=`), and `GTE` (`>=`). These are grouped together with right associativity.

# Bison parsing table generation
## Examples
```python
# First production identifies the start symbol
def p_program(t):
    'program : body'
    interfacing_parser.the_program = AST.function("main", None, t[1], t.lexer.lineno)


def p_empty(t):
    'empty :'
    t[0] = None


def p_body(t):
    'body : optional_variables_declaration_list optional_functions_declaration_list statement_list'
    t[0] = AST.body(t[1], t[2], t[3], t.lexer.lineno)

def p_statement(t):
    '''statement : statement_return
                 | statement_print
                 | statement_assignment
                 | statement_ifthenelse
                 | statement_while
                 | statement_compound'''
    t[0] = t[1]


def p_statement_return(t):
    'statement_return : RETURN expression SEMICOL'
    t[0] = AST.statement_return(t[2], t.lexer.lineno)
```

## Core functionallity
```python
'program : body'
interfacing_parser.the_program = AST.function("main", None, t[1], t.lexer.lineno)
```
This will make a `function-instance` where the `body` is `t[1]`.
Looking into the fact that
```python
def p_body(t):
    'body : optional_variables_declaration_list optional_functions_declaration_list statement_list'
    t[0] = AST.body(t[1], t[2], t[3], t.lexer.lineno)
```
will use `t[0]`, which corresponds to the `body` in the lexer, then when setting `t[0]= xxxxxx` this means we use the reference of the body and update it. 
Therefore, when we have used `t[1]` in `p_program(t)` which corresponds to `body`, and we use `t[0]` in `p_body(t)`, then we update the reference used in `p_program(t)`. This is how we make the tree, by using references, and accessing these via the `t[x]`.
### p_program
The first production, must go to a body. We save it in a `function`-class, and save the value of what `body` returns. This is the `t[1]` part/
### p_body
for the `body` we have defined a class as well, saving each of the ouputs that may arrive from the rules, fx what is returned from `optional_variables_declaration_list` is put into the first variable of the `body`-class and so on.
### p_statement
This production is for the `statement` where it can be be either `statement_return,statement_print...`, and the output is the saved into the node for the production, i.e `t[0]=t[1]`, where `t[1]` is the output from the reduction of the right hand side.
### p_statement_return
this will return a `statement_return`-node, and output depends on the reduction of `expression`, `t[2]` is then `expression`.





# Visitors
## symbol visitor
This is responsible of setting up the symbol table. It saves extra information to the nodes.
### Example
```python
def preVisit_function(self, t):
        # The name of the function belongs to the surrounding scope:
        if t.name != "main":
            if self._current_scope.lookup_this_scope(t.name):
                error_message(
                    "Symbol Collection",
                    f"Redeclaration of function '{t.name}' in the same scope.",
                    t.lineno)
            self._current_scope.insert(
                t.name, SymVal(NameCategory.FUNCTION, self._current_level, t))
        # Parameters and the body of the function belongs to the inner scope:
        self._current_level += 1
        self._current_scope = SymbolTable(self._current_scope)
        # Saving the current symbol table in the AST for future use:
        t.symbol_table = self._current_scope
        t.scope_level = self._current_level
        # Preparing for the processing of formal parameters:
        self.parameter_offset = 0
```
it can be seen that the `symbol_table, scope_level` is added to the node. This can then be used in the next visitors
### Which ASTs are touched in this flow
1. `previsit_function`
	1. if `par_list` call on this
		1. `previt_paramater_list()` this is just inserting the formal parameters into the list
		2. this keeps on going for all of the formal parameters provded
2. `midvist_function()`
	1. setup parameter offset
3. `accept body`
	1. `preVisit_body()` put on information that variable offset is 0
	2. if there are a variable declaration list
		1. `preVisit_variables_list()` multiple times, untill all has been registered in the current scope
	3. `preMidVisit_body()` will just set the number of variables
	4. if `functions_decl`
		1. call again on the entire `previsit_function()` for all functions in the program
	5. `accept statement list`, and there are no statement in the symbol collection phase.
	6. `postvisit` no postvisit in symbol
4. `postvisit_function` nothing happens

#### Finally, classes touched
- Function
- Parameter list 
- body
- Variable_Declation_List
	- variables_list
- functions_declaration_list
	- function
### Structure of symbol collection
it can be seen that the
- `number_of_parameters: int`
- `scope_level: int`
- `symbol_table: SymbolTable`
	- SymbolTable.tab: `Map<String, SymVal>`
	- SymbolTable.parent: `SymbolTable`
is added to the node. This can then be used in the next visitors

- Save function names, variable names, parameter names
	- We use this when we check what we can assign these to
## Type checking
responsible for stopping the compilation if checks are not correct.
### Example
``` python
def postVisit_expression_identifier(self, t):
        value = self._current_scope.lookup(t.identifier)
        if not value:
            error_message("Symbol Collection",
                          f"Identifier '{t.identifier}' not found.",
                          t.lineno)
        if value.cat == NameCategory.FUNCTION:
            error_message(
                "Type Checking",
                f"Function name '{t.identifier}' cannot be an identifier.",
                t.lineno)
```
Here we can see that we use the `symbol collection`-phase, as we want to use the `lookup`, to see if the variable is defined in the current scope, using static scope. I.e it also look up in the parents scope table and its symbol table. See the function:
```python
def lookup(self, name):
        if name in self._tab:
            return self._tab[name]
        elif self.parent:
            return self.parent.lookup(name)
        else:
            return None
```
If we have not defined the variable in the current static scope, then there will be an error message, and if the name of the node corresponds to a function, then we will also print out a error message.
### Key notes to this phase
- `__init__`
	- Allow for current scope
	- Number of actual parameters, used like a stack to determine how many parameters when using nested calls. I.e each nested call should only count as `1`
- `postVisit_statement_assignment()`
	- The identifier has to be in the current static scope, else exception
	- The identifier cannot be a `paramater`, i.e cannot do `func(x = 2)`, where `x` is the identifier (the left hand side) and `2` is the (right hand side)
	- The identifier cannot be a function, i.e cannot do `hello(x, y) = something`, where `hello` is the identifier (the left hand side) and `something` is the (right hand side)
- `postVisit_expression_identifier()`
	- see if the left hand side exists
	- dont allow functions to be identifiers. That is we can do
		- `var x = 2`
		- `var x = y`
		- `func(y, k)`
	- but cannot do
		- `func = 3`
- `preVisit_expression_call()`
	- setups the stack for a new expression, i.e the number of expressions in this expression is `0` to begin with
- `postVisit_expression_call()`
	- Looks up for the function, if not exists -> throw exception.
		- This is called as `postVisit` meaning all of the logic which this needs has already been called, therefore we expect a final state.
		- if there are too few or too many arguments to the function, then we will throw an exception
	- Lastly, since we use `number_of_actual_parameters` as a global/static state, we will have to `.pop()` the number at the last place, since this will not be used anymore.
- `midVisit_expression_list()`
	- This is called many times, incrementing the last actual parameter count.
## Code generation
### Output
Every `Ins` is saved into the `_code` field as an array of `Ins`.
### All about using
- All about using
	- `OP`
		- The operation to do
	- `T`
		- The destination of the execution of the `Ins`
			- Integer
			- Label
			- Memory
			- Register
	- `M`
		- Addressing mode
	- `Target`
		- which `T` to use
		- With optional argument
			- if Label
			- use register `0, 1` or `2`
	- `Mode`
		- Using `M` as the addressing mode and an optional argument
			- Optional argument is used when providing an `offset` into memory
	- `Arg`
		- Used as combined `Target` with `Mode`
	- `Meta`
		- Enums for regularly used assembly
	- `Ins`
		- an instruction with `opcode`
		- multiple `Args` or provide a `Meta`
## Emit
- Go through all of the code, i.e array of `class Ins`, for each of the `class Ins` we go through a switch case,
	- if the `opcode` cannot be directly translated into `assembly x86`.
	- else we go through a switch case where we have to implement the instructions ourselves. 
		- if the `Ins` arg is a `Meta`, then we do predefined actions
			- This could be setting up for a function call with calle-save registers.

