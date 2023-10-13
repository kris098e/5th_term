%{
    
%}

%union {
    char *string;
}
%token <string> id
%start S

%%
S: E;

E: 'while' E 'do' E
    | id '=' E
    | E '+' E
    | id
    ;
%%