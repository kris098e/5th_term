
.data

form:
                .string "%d\n"          # form string for C printf

.text

.globl main

F0000_sum_recurse:

                                        # CALLEE PROLOGUE
                pushq %rbp              # save caller's base pointer
                movq %rsp, %rbp         # make stack pointer new base pointer

                addq $0, %rsp           # allocate space for local variables

                movq %rbp, %rdx         # preparing for static link computation
                pushq 24(%rdx)          # push value of 1. parameter
                pushq $1                # push integer expression
                popq %rcx               # pop 2nd expression to register
                popq %rbx               # pop 1st expression to register
                cmpq %rcx, %rbx         # compare values
                je F0004_cmp_true       # jump if the expression was true
                pushq $0                # push false
                jmp F0005_cmp_end       # done with comparison
F0004_cmp_true:
                pushq $1                # push true
F0005_cmp_end:
                popq %rbx               # move computed boolean to register
                movq $0, %rcx           # move false to register
                cmpq %rbx, %rcx         # compare computed boolean to false
                je F0002_else           # jump to else-part if false
                pushq $1                # push integer expression
                popq %rax               # move return value to return register
                jmp F0001_end_sum_recurse# jump to function epiloque
                jmp F0003_endif         # 
F0002_else:
                movq %rbp, %rdx         # preparing for static link computation
                pushq 24(%rdx)          # push value of 1. parameter
                movq %rbp, %rdx         # preparing for static link computation
                pushq 24(%rdx)          # push value of 1. parameter
                pushq $1                # push integer expression
                popq %rbx               # pop 2nd expression to register
                popq %rcx               # pop 1st expression to register
                subq %rbx, %rcx         # carry out the operation
                pushq %rcx              # push the resulting value
                                        # CALLER PROLOGUE: empty

                pushq 0(%rsp)           # push arguments in reverse order
                movq %rbp, %rdx         # preparing for static link computation
                pushq 16(%rdx)          # set up static link for outer function
                callq F0000_sum_recurse # 
                addq $16, %rsp          # deallocate stack space for parameters
                                        # or local variables

                                        # CALLER EPILOGUE: empty

                addq $8, %rsp           # deallocate stack space for parameters
                                        # or local variables

                pushq %rax              # push return value as the call result
                popq %rbx               # pop 2nd expression to register
                popq %rcx               # pop 1st expression to register
                addq %rbx, %rcx         # carry out the operation
                pushq %rcx              # push the resulting value
                popq %rax               # move return value to return register
                jmp F0001_end_sum_recurse# jump to function epiloque
F0003_endif:
F0001_end_sum_recurse:

                                        # CALLEE EPILOGUE
                movq %rbp, %rsp         # restore stack pointer
                popq %rbp               # restore base pointer
                ret                     # return from call

F0006_sum_loop:

                                        # CALLEE PROLOGUE
                pushq %rbp              # save caller's base pointer
                movq %rsp, %rbp         # make stack pointer new base pointer

                addq $-24, %rsp         # allocate space for local variables

                pushq $9                # push integer expression
                                        # CALLER PROLOGUE: empty

                pushq 0(%rsp)           # push arguments in reverse order
                movq %rbp, %rdx         # preparing for static link computation
                pushq 16(%rdx)          # set up static link for outer function
                callq F0000_sum_recurse # 
                addq $16, %rsp          # deallocate stack space for parameters
                                        # or local variables

                                        # CALLER EPILOGUE: empty

                addq $8, %rsp           # deallocate stack space for parameters
                                        # or local variables

                pushq %rax              # push return value as the call result
                movq %rbp, %rdx         # preparing for static link computation
                popq -24(%rdx)          # assigning the computed expression
                movq %rbp, %rdx         # preparing for static link computation
                pushq -24(%rdx)         # push value of 3. variable
                                        # CALLER PROLOGUE: empty

                                        # PRINTING
                leaq form(%rip), %rdi   # pass 1. argument in %rdi
                movq 0(%rsp), %rsi      # pass 2. argument in %rsi
                movq $0, %rax           # no floating point registers used
                testq $15, %rsp         # test for 16 byte alignment
                jz F0014_aligned        # jump if aligned
                addq $-8, %rsp          # 16 byte aligning
                callq printf@plt        # call printf
                addq $8, %rsp           # reverting alignment
                jmp F0015_end_aligned   # 
F0014_aligned:
                callq printf@plt        # call printf
F0015_end_aligned:

                                        # CALLER EPILOGUE: empty

                addq $8, %rsp           # pop expression from stack

                pushq $1                # push integer expression
                movq %rbp, %rdx         # preparing for static link computation
                popq -16(%rdx)          # assigning the computed expression
                pushq $0                # push integer expression
                movq %rbp, %rdx         # preparing for static link computation
                popq -8(%rdx)           # assigning the computed expression
F0008_while:
                movq %rbp, %rdx         # preparing for static link computation
                pushq -16(%rdx)         # push value of 2. variable
                movq %rbp, %rdx         # preparing for static link computation
                pushq 24(%rdx)          # push value of 1. parameter
                popq %rcx               # pop 2nd expression to register
                popq %rbx               # pop 1st expression to register
                cmpq %rcx, %rbx         # compare values
                jle F0010_cmp_true      # jump if the expression was true
                pushq $0                # push false
                jmp F0011_cmp_end       # done with comparison
F0010_cmp_true:
                pushq $1                # push true
F0011_cmp_end:
                popq %rbx               # move computed boolean to register
                movq $0, %rcx           # move false to register
                cmpq %rbx, %rcx         # compare computed boolean to false
                je F0009_endwhile       # jump to end_while if false
                movq %rbp, %rdx         # preparing for static link computation
                pushq -8(%rdx)          # push value of 1. variable
                movq %rbp, %rdx         # preparing for static link computation
                pushq -16(%rdx)         # push value of 2. variable
                popq %rbx               # pop 2nd expression to register
                popq %rcx               # pop 1st expression to register
                addq %rbx, %rcx         # carry out the operation
                pushq %rcx              # push the resulting value
                movq %rbp, %rdx         # preparing for static link computation
                popq -8(%rdx)           # assigning the computed expression
                movq %rbp, %rdx         # preparing for static link computation
                pushq -16(%rdx)         # push value of 2. variable
                pushq $1                # push integer expression
                popq %rbx               # pop 2nd expression to register
                popq %rcx               # pop 1st expression to register
                addq %rbx, %rcx         # carry out the operation
                pushq %rcx              # push the resulting value
                movq %rbp, %rdx         # preparing for static link computation
                popq -16(%rdx)          # assigning the computed expression
                jmp F0008_while         # 
F0009_endwhile:
                movq %rbp, %rdx         # preparing for static link computation
                pushq -8(%rdx)          # push value of 1. variable
                popq %rax               # move return value to return register
                jmp F0007_end_sum_loop  # jump to function epiloque
F0007_end_sum_loop:

                                        # CALLEE EPILOGUE
                movq %rbp, %rsp         # restore stack pointer
                popq %rbp               # restore base pointer
                ret                     # return from call

F0012_hello:

                                        # CALLEE PROLOGUE
                pushq %rbp              # save caller's base pointer
                movq %rsp, %rbp         # make stack pointer new base pointer

                addq $0, %rsp           # allocate space for local variables

                movq %rbp, %rdx         # preparing for static link computation
                pushq 24(%rdx)          # push value of 1. parameter
                popq %rax               # move return value to return register
                jmp F0013_end_hello     # jump to function epiloque
F0013_end_hello:

                                        # CALLEE EPILOGUE
                movq %rbp, %rsp         # restore stack pointer
                popq %rbp               # restore base pointer
                ret                     # return from call

main:

                                        # CALLEE PROLOGUE
                pushq %rbp              # save caller's base pointer
                movq %rsp, %rbp         # make stack pointer new base pointer

                addq $0, %rsp           # allocate space for local variables


                pushq %rbx              # %rbx is callee save
                pushq %r12              # %r12 is callee save
                pushq %r13              # %r13 is callee save
                pushq %r14              # %r14 is callee save
                pushq %r15              # %r15 is callee save

                pushq $9                # push integer expression
                                        # CALLER PROLOGUE: empty

                pushq 0(%rsp)           # push arguments in reverse order
                pushq %rbp              # set up static link for inner function
                callq F0000_sum_recurse # 
                addq $16, %rsp          # deallocate stack space for parameters
                                        # or local variables

                                        # CALLER EPILOGUE: empty

                addq $8, %rsp           # deallocate stack space for parameters
                                        # or local variables

                pushq %rax              # push return value as the call result
                                        # CALLER PROLOGUE: empty

                                        # PRINTING
                leaq form(%rip), %rdi   # pass 1. argument in %rdi
                movq 0(%rsp), %rsi      # pass 2. argument in %rsi
                movq $0, %rax           # no floating point registers used
                testq $15, %rsp         # test for 16 byte alignment
                jz F0016_aligned        # jump if aligned
                addq $-8, %rsp          # 16 byte aligning
                callq printf@plt        # call printf
                addq $8, %rsp           # reverting alignment
                jmp F0017_end_aligned   # 
F0016_aligned:
                callq printf@plt        # call printf
F0017_end_aligned:

                                        # CALLER EPILOGUE: empty

                addq $8, %rsp           # pop expression from stack

                pushq $9                # push integer expression
                                        # CALLER PROLOGUE: empty

                pushq 0(%rsp)           # push arguments in reverse order
                pushq %rbp              # set up static link for inner function
                callq F0006_sum_loop    # 
                addq $16, %rsp          # deallocate stack space for parameters
                                        # or local variables

                                        # CALLER EPILOGUE: empty

                addq $8, %rsp           # deallocate stack space for parameters
                                        # or local variables

                pushq %rax              # push return value as the call result
                                        # CALLER PROLOGUE: empty

                                        # PRINTING
                leaq form(%rip), %rdi   # pass 1. argument in %rdi
                movq 0(%rsp), %rsi      # pass 2. argument in %rsi
                movq $0, %rax           # no floating point registers used
                testq $15, %rsp         # test for 16 byte alignment
                jz F0018_aligned        # jump if aligned
                addq $-8, %rsp          # 16 byte aligning
                callq printf@plt        # call printf
                addq $8, %rsp           # reverting alignment
                jmp F0019_end_aligned   # 
F0018_aligned:
                callq printf@plt        # call printf
F0019_end_aligned:

                                        # CALLER EPILOGUE: empty

                addq $8, %rsp           # pop expression from stack

                pushq $42               # push integer expression
                                        # CALLER PROLOGUE: empty

                pushq 0(%rsp)           # push arguments in reverse order
                pushq %rbp              # set up static link for inner function
                callq F0000_sum_recurse # 
                addq $16, %rsp          # deallocate stack space for parameters
                                        # or local variables

                                        # CALLER EPILOGUE: empty

                addq $8, %rsp           # deallocate stack space for parameters
                                        # or local variables

                pushq %rax              # push return value as the call result
                                        # CALLER PROLOGUE: empty

                                        # PRINTING
                leaq form(%rip), %rdi   # pass 1. argument in %rdi
                movq 0(%rsp), %rsi      # pass 2. argument in %rsi
                movq $0, %rax           # no floating point registers used
                testq $15, %rsp         # test for 16 byte alignment
                jz F0020_aligned        # jump if aligned
                addq $-8, %rsp          # 16 byte aligning
                callq printf@plt        # call printf
                addq $8, %rsp           # reverting alignment
                jmp F0021_end_aligned   # 
F0020_aligned:
                callq printf@plt        # call printf
F0021_end_aligned:

                                        # CALLER EPILOGUE: empty

                addq $8, %rsp           # pop expression from stack

                pushq $42               # push integer expression
                                        # CALLER PROLOGUE: empty

                pushq 0(%rsp)           # push arguments in reverse order
                pushq %rbp              # set up static link for inner function
                callq F0006_sum_loop    # 
                addq $16, %rsp          # deallocate stack space for parameters
                                        # or local variables

                                        # CALLER EPILOGUE: empty

                addq $8, %rsp           # deallocate stack space for parameters
                                        # or local variables

                pushq %rax              # push return value as the call result
                                        # CALLER PROLOGUE: empty

                                        # PRINTING
                leaq form(%rip), %rdi   # pass 1. argument in %rdi
                movq 0(%rsp), %rsi      # pass 2. argument in %rsi
                movq $0, %rax           # no floating point registers used
                testq $15, %rsp         # test for 16 byte alignment
                jz F0022_aligned        # jump if aligned
                addq $-8, %rsp          # 16 byte aligning
                callq printf@plt        # call printf
                addq $8, %rsp           # reverting alignment
                jmp F0023_end_aligned   # 
F0022_aligned:
                callq printf@plt        # call printf
F0023_end_aligned:

                                        # CALLER EPILOGUE: empty

                addq $8, %rsp           # pop expression from stack

                pushq $2                # push integer expression
                                        # CALLER PROLOGUE: empty

                pushq 0(%rsp)           # push arguments in reverse order
                pushq %rbp              # set up static link for inner function
                callq F0012_hello       # 
                addq $16, %rsp          # deallocate stack space for parameters
                                        # or local variables

                                        # CALLER EPILOGUE: empty

                addq $8, %rsp           # deallocate stack space for parameters
                                        # or local variables

                pushq %rax              # push return value as the call result
                pushq $0                # push integer expression
                popq %rax               # move return value to return register
                jmp end_main            # jump to function epiloque
end_main:

                popq %r15               # restore callee save register
                popq %r14               # restore callee save register
                popq %r13               # restore callee save register
                popq %r12               # restore callee save register
                popq %rbx               # restore callee save register


                                        # CALLEE EPILOGUE
                movq %rbp, %rsp         # restore stack pointer
                popq %rbp               # restore base pointer
                ret                     # return from call



