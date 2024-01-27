%{
#include <stdio.h>
#include "y.tab.h"
void yyerror (char *s);
int yylex();
%}
%option nounput yylineno

%%
c   { return 'c'; }
d   { return 'd'; }
b   { return 'b'; }
%%

int yywrap(void) // boilerplate, used when parsing multiple files.
{
	return 1;
}
