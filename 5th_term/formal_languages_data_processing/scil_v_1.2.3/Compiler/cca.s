
.data

form:
                .string "%d\n"          # form string for C _printf

.text

.globl _main

F0000_f:

                                        # CALLEE PROLOGUE
                pushq %rbp              # save caller's base pointer
                movq %rsp, %rbp         # make stack pointer new base pointer

                addq $0, %rsp           # allocate space for local variables

                movq %rbp, %rdx         # preparing for static link computation
                movq 16(%rdx), %rdx     # following the static link
                pushq -8(%rdx)          # push value of 1. variable
                movq %rbp, %rdx         # preparing for static link computation
                pushq 24(%rdx)          # push value of 1. parameter
                popq %rbx               # pop 2nd expression to register
                popq %rcx               # pop 1st expression to register
                addq %rbx, %rcx         # carry out the operation
                pushq %rcx              # push the resulting value
                movq %rbp, %rdx         # preparing for static link computation
                movq 16(%rdx), %rdx     # following the static link
                popq -8(%rdx)           # assigning the computed expression
                pushq $0                # push integer expression
                popq %rax               # move return value to return register
                jmp F0001_end_f         # jump to function epiloque
F0001_end_f:

                                        # CALLEE EPILOGUE
                movq %rbp, %rsp         # restore stack pointer
                popq %rbp               # restore base pointer
                ret                     # return from call

_main:

                                        # CALLEE PROLOGUE
                pushq %rbp              # save caller's base pointer
                movq %rsp, %rbp         # make stack pointer new base pointer

                addq $-8, %rsp          # allocate space for local variables


                pushq %rbx              # %rbx is callee save
                pushq %r12              # %r12 is callee save
                pushq %r13              # %r13 is callee save
                pushq %r14              # %r14 is callee save
                pushq %r15              # %r15 is callee save

                pushq $0                # push integer expression
                movq %rbp, %rdx         # preparing for static link computation
                popq -8(%rdx)           # assigning the computed expression
                pushq $39               # push integer expression
                pushq $3                # push integer expression
                pushq $0                # push integer expression
                                        # CALLER PROLOGUE: empty

                pushq 0(%rsp)           # push arguments in reverse order
                pushq 16(%rsp)          # push arguments in reverse order
                pushq %rbp              # set up static link for inner function
                call F0000_f           # 
                addq $24, %rsp          # deallocate stack space for parameters
                                        # or local variables

                                        # CALLER EPILOGUE: empty

                addq $16, %rsp          # deallocate stack space for parameters
                                        # or local variables

                pushq %rax              # push return value as the call result
                pushq $1                # push integer expression
                                        # CALLER PROLOGUE: empty

                pushq 0(%rsp)           # push arguments in reverse order
                pushq 16(%rsp)          # push arguments in reverse order
                pushq %rbp              # set up static link for inner function
                call F0000_f           # 
                addq $24, %rsp          # deallocate stack space for parameters
                                        # or local variables

                                        # CALLER EPILOGUE: empty

                addq $16, %rsp          # deallocate stack space for parameters
                                        # or local variables

                pushq %rax              # push return value as the call result
                                        # CALLER PROLOGUE: empty

                pushq 0(%rsp)           # push arguments in reverse order
                pushq 16(%rsp)          # push arguments in reverse order
                pushq %rbp              # set up static link for inner function
                call F0000_f           # 
                addq $24, %rsp          # deallocate stack space for parameters
                                        # or local variables

                                        # CALLER EPILOGUE: empty

                addq $16, %rsp          # deallocate stack space for parameters
                                        # or local variables

                pushq %rax              # push return value as the call result
                                        # CALLER PROLOGUE: empty

                                        # PRINTING
                leaq form(%rip), %rdi   # pass 1. argument in %rdi
                movq 0(%rsp), %rsi      # pass 2. argument in %rsi
                movq $0, %rax           # no floating point registers used
                testq $15, %rsp         # test for 16 byte alignment
                jz F0002_aligned        # jump if aligned
                addq $-8, %rsp          # 16 byte aligning
                call _printf        # call printf
                addq $8, %rsp           # reverting alignment
                jmp F0003_end_aligned   # 
F0002_aligned:
                call _printf        # call printf
F0003_end_aligned:

                                        # CALLER EPILOGUE: empty

                addq $8, %rsp           # pop expression from stack

                movq %rbp, %rdx         # preparing for static link computation
                pushq -8(%rdx)          # push value of 1. variable
                                        # CALLER PROLOGUE: empty

                                        # PRINTING
                leaq form(%rip), %rdi   # pass 1. argument in %rdi
                movq 0(%rsp), %rsi      # pass 2. argument in %rsi
                movq $0, %rax           # no floating point registers used
                testq $15, %rsp         # test for 16 byte alignment
                jz F0004_aligned        # jump if aligned
                addq $-8, %rsp          # 16 byte aligning
                call _printf        # call printf
                addq $8, %rsp           # reverting alignment
                jmp F0005_end_aligned   # 
F0004_aligned:
                call _printf        # call printf
F0005_end_aligned:

                                        # CALLER EPILOGUE: empty

                addq $8, %rsp           # pop expression from stack

                pushq $0                # push integer expression
                popq %rax               # move return value to return register
                jmp end__main            # jump to function epiloque
end__main:

                popq %r15               # restore callee save register
                popq %r14               # restore callee save register
                popq %r13               # restore callee save register
                popq %r12               # restore callee save register
                popq %rbx               # restore callee save register


                                        # CALLEE EPILOGUE
                movq %rbp, %rsp         # restore stack pointer
                popq %rbp               # restore base pointer
                ret                     # return from call



