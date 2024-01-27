%{
    #include <stdio.h>

    int yylex();

    void yyerror(char *s) {
        printf("syntax error before %s\n", "hej"); 
    }
%}

// %union{void v;}
// %type<v> S B D 
%start S

%%
    S: B 'c' {printf("1");}
    ;

    B: D B {printf("2");}
        | 'b' {printf("3");}
    ;
    D: 'd' {printf("4");}
    ;
%%

int main(void) { return yyparse(); }