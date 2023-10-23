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
it can be seen that fx the `symbol_table, scope_level` is added to the node. This can then be used in the next visitors
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
