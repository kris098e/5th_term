[[06-compiler.pdf]]

remember to read the code and understand the code, as this will help a lot
# Compiler phases
page 3
## Frontend
error detection
### Scanner
takes input program character by character, returns tokens of interest
### Parser
takes the tokens, are these allowed in the programming language and are they correctly placed
### Symbol Collection
identifiers collection
### Type checking
staticly done before, or begin executing
## Back end
Generate the ouput
### Code generation
produce assembler code or other output we want.
here we can also do some optimization
### Emit
finally emit the code which can be ran, or the output

