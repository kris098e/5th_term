%{
    
%}

%union {
    char *string;
}
%token <string> id
%type <string> S
%start S

%%
S: E; { $$ = $1 }

E: 'while' E 'do' E
    | id '=' E
    | E '+' E
    | id
    ;
%%