# intro
![[Pasted image 20240121112226.png]]
- y.tab.h is the types the `yacc` compiler expects in the context free grammar
![[Pasted image 20240121112255.png]]
![[Pasted image 20240121112453.png]]
- `%start` is the first statement in the context free grammar
- `%token` is the tokens
- `%union` can specify a union
- `%type` specify types
![[Pasted image 20240121112556.png]]
![[Pasted image 20240121112729.png]]
![[Pasted image 20240121113124.png]]
![[Pasted image 20240121113217.png]]
![[Pasted image 20240121113332.png]]
# Example
```c
%{
void yyerror (char *s);
int yylex();
#include <stdio.h>     /* C declarations used in actions */
#include <stdlib.h>
#include <ctype.h>
int symbols[52]; // symbol table
int symbolVal(char symbol); // helper function
void updateSymbolVal(char symbol, int val); // helper function
%}

/* Yacc definitions */
%union {int num; char id;}         // what types we can have in the program
%start line // starting production
%token print // token
%token exit_command // token
%token <num> number // whenever we see a number, it is going to be assigned to the `num` in the %union
%token <id> identifier // whenever we see an identifier, it is going to be assigned to the `id` in the %union
%type <num> line exp term  // line, exp, term will all return something of type int, as `num` is in the union
%type <id> assignment // assignment will return something of type string, as `id` is in the union

%%

/* descriptions of expected inputs     corresponding actions (in C) */

line    : assignment ';'		{;} // assignment will handle the logic, dont do anything
		| exit_command ';'		{exit(EXIT_SUCCESS);} // exit
		| print exp ';'			{printf("Printing %d\n", $2);} // we know `exp` is an int
// These next recursive definitions are what let us have multiple lines. If we did not call `line` again, we would simply only be allowed to enter a single `line`.
		| line assignment ';'	{;} // assignment handle the logic
		| line print exp ';'	{printf("Printing %d\n", $3);} // we know know exp is an int
		| line exit_command ';'	{exit(EXIT_SUCCESS);} // exit
        ;

assignment : identifier '=' exp  { updateSymbolVal($1,$3); } // call the function
			;
exp    	: term                  {$$ = $1;} // save 
       	| exp '+' term          {$$ = $1 + $3;} // can have multiple `exp` ending with a term
       	| exp '-' term          {$$ = $1 - $3;} // same
       	;
term   	: number                {$$ = $1;} // save
		| identifier			{$$ = symbolVal($1);} // save
        ;

%%                     /* C code */

int computeSymbolIndex(char token)
{
	int idx = -1;
	if(islower(token)) {
		idx = token - 'a' + 26;
	} else if(isupper(token)) {
		idx = token - 'A';
	}
	return idx;
} 

/* returns the value of a given symbol */
int symbolVal(char symbol)
{
	int bucket = computeSymbolIndex(symbol);
	return symbols[bucket];
}

/* updates the value of a given symbol */
void updateSymbolVal(char symbol, int val)
{
	int bucket = computeSymbolIndex(symbol);
	symbols[bucket] = val;
}

int main (void) {
	/* init symbol table */
	int i;
	for(i=0; i<52; i++) {
		symbols[i] = 0; // initialise all symbols to 0
	}

	return yyparse ( ); //actual parser
}

void yyerror (char *s) {fprintf (stderr, "%s\n", s);} // this is called whenever we see a syntax error
```

```c
%{
#include "y.tab.h"
void yyerror (char *s);
int yylex();
%}
%%
"print"				   {return print;} // print is defined as a token inside y.tab.h
"exit"				   {return exit_command;}} // exit_command defined inside y.tab.h
[a-zA-Z]			   {yylval.id = yytext[0]; return identifier;} //use the `id` in the union. The id can only be 1 char long. return the terminal symbol
[0-9]+                 {yylval.num = atoi(yytext); return number;} // use `num` in union. return the terminal symbol
[ \t\n]                ;
[-+=;]           	   {return yytext[0];} // this is just accessed inside of the context free grammer with '
.                      {ECHO; yyerror ("unexpected character");}

%%
int yywrap (void) {return 1;}
```

![[Pasted image 20240121115936.png]]
Will generate the `y.tab.h` with the `-d` option, and the `.c` file
![[Pasted image 20240121120015.png]]
compile lex

![[Pasted image 20240121120042.png]]
compile them together.

