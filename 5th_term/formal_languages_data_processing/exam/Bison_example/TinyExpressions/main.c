#include <stdio.h>
#include "tree.h"
#include "pretty.h"

int lineno;

void yyparse();

EXP *theexpression;

int main()
{ lineno = 1;
  yyparse();
  prettyEXP(theexpression);
  printf("\n");
  return 0;
}
