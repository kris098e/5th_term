
.data

form:
                .string "%d\n"          # form string for C printf

.text

.globl main

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

                pushq $41               # push integer expression
                pushq $1                # push integer expression
                popq %rbx               # pop 2nd expression to register
                popq %rcx               # pop 1st expression to register
                addq %rbx, %rcx         # carry out the operation
                pushq %rcx              # push the resulting value
                                        # CALLER PROLOGUE: empty

                                        # PRINTING
                leaq form(%rip), %rdi   # pass 1. argument in %rdi
                movq 0(%rsp), %rsi      # pass 2. argument in %rsi
                movq $0, %rax           # no floating point registers used
                testq $15, %rsp         # test for 16 byte alignment
                jz F0000_aligned        # jump if aligned
                addq $-8, %rsp          # 16 byte aligning
                callq printf@plt        # call printf
                addq $8, %rsp           # reverting alignment
                jmp F0001_end_aligned   # 
F0000_aligned:
                callq printf@plt        # call printf
F0001_end_aligned:

                                        # CALLER EPILOGUE: empty

                addq $8, %rsp           # pop expression from stack

                pushq $43               # push integer expression
                pushq $1                # push integer expression
                popq %rbx               # pop 2nd expression to register
                popq %rcx               # pop 1st expression to register
                subq %rbx, %rcx         # carry out the operation
                pushq %rcx              # push the resulting value
                                        # CALLER PROLOGUE: empty

                                        # PRINTING
                leaq form(%rip), %rdi   # pass 1. argument in %rdi
                movq 0(%rsp), %rsi      # pass 2. argument in %rsi
                movq $0, %rax           # no floating point registers used
                testq $15, %rsp         # test for 16 byte alignment
                jz F0002_aligned        # jump if aligned
                addq $-8, %rsp          # 16 byte aligning
                callq printf@plt        # call printf
                addq $8, %rsp           # reverting alignment
                jmp F0003_end_aligned   # 
F0002_aligned:
                callq printf@plt        # call printf
F0003_end_aligned:

                                        # CALLER EPILOGUE: empty

                addq $8, %rsp           # pop expression from stack

                pushq $6                # push integer expression
                pushq $7                # push integer expression
                popq %rbx               # pop 2nd expression to register
                popq %rcx               # pop 1st expression to register
                imulq %rbx, %rcx        # carry out the operation
                pushq %rcx              # push the resulting value
                                        # CALLER PROLOGUE: empty

                                        # PRINTING
                leaq form(%rip), %rdi   # pass 1. argument in %rdi
                movq 0(%rsp), %rsi      # pass 2. argument in %rsi
                movq $0, %rax           # no floating point registers used
                testq $15, %rsp         # test for 16 byte alignment
                jz F0004_aligned        # jump if aligned
                addq $-8, %rsp          # 16 byte aligning
                callq printf@plt        # call printf
                addq $8, %rsp           # reverting alignment
                jmp F0005_end_aligned   # 
F0004_aligned:
                callq printf@plt        # call printf
F0005_end_aligned:

                                        # CALLER EPILOGUE: empty

                addq $8, %rsp           # pop expression from stack

                pushq $84               # push integer expression
                pushq $2                # push integer expression
                popq %rbx               # pop 2nd expression to register
                popq %rcx               # pop 1st expression to register
                movq %rcx, %rax         # prepare for division
                cqo                     # sign extend
                idivq %rbx              # divide
                movq %rax, %rcx         # move to destination
                pushq %rcx              # push the resulting value
                                        # CALLER PROLOGUE: empty

                                        # PRINTING
                leaq form(%rip), %rdi   # pass 1. argument in %rdi
                movq 0(%rsp), %rsi      # pass 2. argument in %rsi
                movq $0, %rax           # no floating point registers used
                testq $15, %rsp         # test for 16 byte alignment
                jz F0006_aligned        # jump if aligned
                addq $-8, %rsp          # 16 byte aligning
                callq printf@plt        # call printf
                addq $8, %rsp           # reverting alignment
                jmp F0007_end_aligned   # 
F0006_aligned:
                callq printf@plt        # call printf
F0007_end_aligned:

                                        # CALLER EPILOGUE: empty

                addq $8, %rsp           # pop expression from stack

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



