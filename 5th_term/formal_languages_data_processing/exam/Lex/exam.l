%{
#include <stdio.h>
%}
%option nounput yylineno

%%
[a-c]* {printf("1");}
ac  {printf("2");}
a   {printf("3");}
acd {printf("4");}
da  {printf("5");}

%%

int yywrap(void) // boilerplate, used when parsing multiple files.
{
	return 1;
}

void main() { yylex(); } 