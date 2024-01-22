![[Pasted image 20240121102000.png]]
![[Pasted image 20240121102008.png]]
![[Pasted image 20240121101948.png]]
# Examples
## input
![[Pasted image 20240121102035.png]]
## Header file
```c
#define TYPE 1
#define NAME 2
#define TABLE_PREFIX 3
#define PORT 4
#define COLON 5
#define IDENTIFIER 6
#define INTEGER 7
```
## lex file
```c
%{
#include "myscanner.h"
%}
%option nounput yylineno

%%
:					return COLON;
"db_type"			return TYPE;
"db_name"			return NAME;
"db_table_prefix"	return TABLE_PREFIX;
"db_port"			return PORT;

[a-zA-Z][_a-zA-Z0-9]*	return IDENTIFIER;
[1-9][0-9]*				return INTEGER;
[ \t\n]					;
.					printf("unexpected character\n");

%%

int yywrap(void) // boilerplate, used when parsing multiple files.
{
	return 1;
}
```
## Scanner C
```c
#include <stdio.h>
#include "myscanner.h" // defined types, used in the lexxer parse

extern int yylex(); // comes from lex
extern int yylineno; // comes from lex
extern char* yytext; // comes from lex

char *names[] = {NULL, "db_type", "db_name", "db_table_prefix", "db_port"};

int main(void) 
{

	int ntoken, vtoken; // nameToken and valueToken

	ntoken = yylex(); // read in the first token
	while(ntoken) {
		printf("%d\n", ntoken); // this is an integer due to lex returning the types defined in `myscanner.h`
		if(yylex() != COLON) { // after reading the first token, the next has to be a colon
			printf("Syntax error in line %d, Expected a ':' but found %s\n", yylineno, yytext);
			return 1;
		}
		vtoken = yylex(); // what the type of the value is to this key, which is stored in the nToken
		switch (ntoken) {
		case TYPE:
		case NAME:
		case TABLE_PREFIX:
			if(vtoken != IDENTIFIER) {
				printf("Syntax error in line %d, Expected an identifier but found %s\n", yylineno, yytext);
				return 1;
			}
			printf("%s is set to %s\n", names[ntoken], yytext); // can retrieve the text value by using the extern yytext
			break;
		case PORT:
			if(vtoken != INTEGER) {
				printf("Syntax error in line %d, Expected an integer but found %s\n", yylineno, yytext);
				return 1;
			}
			printf("%s is set to %s\n", names[ntoken], yytext); // again taking the text value by using the extern yytext
			break;
		default:
			printf("Syntax error in line %d\n",yylineno);
		}
		ntoken = yylex(); // next token
	}
	return 0;
}
```
## Running the compiler
![[Pasted image 20240121105355.png]]
Take the outputted lex parser and link it with the scanner
