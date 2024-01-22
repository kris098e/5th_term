
# This module provides class definitions for all the node types in the
# abstract syntax tree (AST). Each node accepts a visitor via its
# accept method, which implements a generic recursive traversal of
# the AST, calling preVisit, postVisit, and other visits at appropriate
# times, relative to the recursive traversals of the children. See
# the module visitors_base for how concrete visitors are dispatched.
# For type annotations, we have used "Any" for entries into the AST.
# The alternative was string versions of the type, since these are
# defined in a mutually recursive fashion, but the variable names
# indicate clearly which AST node it is referring to.


from dataclasses import dataclass
from typing import Any


@dataclass
class body:
    variables_decl: Any
    functions_decl: Any
    stm_list: Any
    lineno: int

    def accept(self, visitor):
        visitor.preVisit(self)
        if self.variables_decl:
            self.variables_decl.accept(visitor)
        visitor.preMidVisit(self)
        if self.functions_decl:
            self.functions_decl.accept(visitor)
        visitor.postMidVisit(self)
        self.stm_list.accept(visitor)
        visitor.postVisit(self)


@dataclass
class variables_declaration_list:
    decl: Any
    next: Any
    lineno: int

    def accept(self, visitor):
        visitor.preVisit(self)
        self.decl.accept(visitor)
        if self.next:
            self.next.accept(visitor)
        visitor.postVisit(self)


@dataclass
class functions_declaration_list:
    decl: Any
    next: Any
    lineno: int

    def accept(self, visitor):
        visitor.preVisit(self)
        self.decl.accept(visitor)
        if self.next:
            self.next.accept(visitor)
        visitor.postVisit(self)


@dataclass
class function:
    name: Any
    par_list: Any
    body: Any
    lineno: int

    def accept(self, visitor):
        visitor.preVisit(self)
        if self.par_list:
            self.par_list.accept(visitor)
        visitor.midVisit(self)
        self.body.accept(visitor)
        visitor.postVisit(self)


@dataclass
class parameter_list:
    parameter: Any
    next: Any
    lineno: int

    def accept(self, visitor):
        visitor.preVisit(self)
        if self.next:
            self.next.accept(visitor)
        visitor.postVisit(self)


@dataclass
class variables_list:
    variable: Any
    next: Any
    lineno: int

    def accept(self, visitor):
        visitor.preVisit(self)
        if self.next:
            self.next.accept(visitor)
        visitor.postVisit(self)


@dataclass
class statement_return:
    exp: Any
    lineno: int

    def accept(self, visitor):
        visitor.preVisit(self)
        self.exp.accept(visitor)
        visitor.postVisit(self)


@dataclass
class statement_print:
    exp: Any
    lineno: int

    def accept(self, visitor):
        visitor.preVisit(self)
        self.exp.accept(visitor)
        visitor.postVisit(self)


@dataclass
class statement_assignment:
    lhs: Any
    rhs: Any
    lineno: int

    def accept(self, visitor):
        visitor.preVisit(self)
        self.rhs.accept(visitor)
        visitor.postVisit(self)


@dataclass
class statement_ifthenelse:
    exp: Any
    then_part: Any
    else_part: Any
    lineno: int

    def accept(self, visitor):
        visitor.preVisit(self)
        self.exp.accept(visitor)
        visitor.preMidVisit(self)
        self.then_part.accept(visitor)
        visitor.postMidVisit(self)
        self.else_part.accept(visitor)
        visitor.postVisit(self)


@dataclass
class statement_while:
    exp: Any
    while_part: Any
    lineno: int

    def accept(self, visitor):
        visitor.preVisit(self)
        self.exp.accept(visitor)
        visitor.midVisit(self)
        self.while_part.accept(visitor)
        visitor.postVisit(self)


@dataclass
class statement_list:
    stm: Any
    next: Any
    lineno: int

    def accept(self, visitor):
        visitor.preVisit(self)
        self.stm.accept(visitor)
        if self.next:
            self.next.accept(visitor)
        visitor.postVisit(self)


@dataclass
class expression_integer:
    integer: int
    lineno: int

    def accept(self, visitor):
        visitor.postVisit(self)


@dataclass
class expression_identifier:
    identifier: str
    lineno: int

    def accept(self, visitor):
        visitor.postVisit(self)


@dataclass
class expression_call:
    name: str
    exp_list: Any
    lineno: int

    def accept(self, visitor):
        visitor.preVisit(self)
        if self.exp_list:
            self.exp_list.accept(visitor)
        visitor.postVisit(self)


@dataclass
class expression_binop:
    op: str
    lhs: Any
    rhs: Any
    lineno: int

    def accept(self, visitor):
        visitor.preVisit(self)
        self.lhs.accept(visitor)
        visitor.midVisit(self)
        self.rhs.accept(visitor)
        visitor.postVisit(self)


@dataclass
class expression_list:
    exp: Any
    next: Any
    lineno: int

    def accept(self, visitor):
        visitor.preVisit(self)
        self.exp.accept(visitor)
        visitor.midVisit(self)
        if self.next:
            self.next.accept(visitor)
        visitor.postVisit(self)
