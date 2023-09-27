[[06-compiler.pdf]]
from page 7

# Input
# Output
fx having `<=` will be send as `LEQ` as this is easier parsed later
# Crafting a scanner
easy to write regular expressions to match some identifiers

make NFAs and turn them into DFAs

have to think about **all** cases to match on
## Regular expression behaviour
enclosing something inside of `""` means we mean the literal string, i.e we dont have to escape any special characters
## Prioritzation rules
1. longest match 
2. first match
Take the longest match first, ie `if42` will take 4 symbols and `if` will take 2 symbols, so take if42 as an identifier

if the two has the same amount of symbols, then we take the first match in the **prioritized list of regular expressions**

## converting the regular expressions
we convert each of the given regular expressions to a `DFA`
_see page 13_
### Convert to NFA
_see page 14_
to combine all of the DFA's
## Running the DFA
keep track of your last final, and report this back if the current state fails and we are not in an accept state

Whenever we cannot go further in the current DFA report the `last final` back and start from scratch

we want them in DFAs as this is more efficient to run

Mark each state with its given token, fx IF, ID, ...
![[Pasted image 20230925105804.png]]
Keep track of where we are, and if we have multiple accept state, `follow the prioritization list`

# Flex
makes the entire last step easier, just write some different format code
## Format
![[Pasted image 20230925111222.png]]
## Run
![[Pasted image 20230925112030.png]]
## Syntax
Have initial state, and from this initial state we can begin fx `comment` and when we are in a `comment` we then do something specific. This becomes more readable and flexible

Can choose any identifier word you want, i.e **dont have to use `Initial` or `COMMENT`** can use anything you want
### Page
see page 24

## Python flex package
can do all sorts of things :)
`lexer`