
from sys import stdin, exit


max_stack_size = 100000


class Stack:
    def __init__(self):
        self.stack = max_stack_size * [0]

    def push(self, x):
        registers[5] -= 8  # Adjusting %rsp
        if self.size() <= len(self.stack):
            self.stack[self.size() - 1] = x
        else:
            error("Out of stack memory.")

    def pop(self):
        registers[5] += 8  # Adjusting %rsp
        return self.stack[self.size()]

    def size(self):
        return spcvrt(registers[5]) + 1  # %rsp converted to internal

    def top(self):
        return self.stack[spcvrt(registers[5])]  # %rsp converted to internal

    def get(self, i):
        return self.stack[spcvrt(i)]  # %rsp converted to internal

    def put(self, i, x):
        self.stack[spcvrt(i)] = x  # %rsp converted to internal

    def print(self):
        for i in range(self.size()):
            print(self.stack[i], end=' ')
        print


def spcvrt(x):
    return int(-x / 8)


def error(message):
    print(message)
    exit(1)


def iError():
    error("We should not be able to end here on scil-generated assembly!")


def parseArgument(text):
    text = text.strip()
    location = text
    indirect = False
    offset = 0
    pos = text.find("(")
    if pos > -1:
        indirect = True
        endpos = text.find(")", pos)
        location = text[pos+1:endpos]
        text = text[:pos].strip()
        if text:
            offset = int(text)
    return (location, indirect, offset)


def parse(text):
    code = []
    pc = 0  # Next free space in code
    labels = {}
    for line in text:
        line = line.split("#", 1)[0]  # Remove trailing comments
        line = line.strip()
        if not line or line.startswith(".") or line.startswith("form:") \
           or line == "leaq form(%rip), %rdi" or line == "movq $form, %rdi":
            continue
        if line[-1] == ":":  # Labels are alone on their lines
            labels[line[:-1]] = pc
            continue
        parts = line.split(" ", 1)
        opcode = parts[0]
        arguments = []
        if len(parts) > 1:
            arguments = list(map(lambda x: x.strip(), parts[1].split(",")))
        code.append((opcode, list(map(parseArgument, arguments))))
        pc += 1
    return (code, labels)


def getVal(argument):
    (location, indirect, offset) = argument
    if location in registerNames:
        content = registers[registerNames.index(location)]
    elif location[0] == "$":
        content = int(location[1:])
    else:
        iError()
    if not indirect:
        return content
    else:
        return stack.get(content + offset)


def putVal(argument, val):
    (location, indirect, offset) = argument
    if location in registerNames:
        i = registerNames.index(location)
    else:
        iError()
    if not indirect:
        registers[i] = val
    else:
        stack.put(registers[i] + offset, val)


def run(code, labels):
    pc = labels["main"]
    flags = {"eq": False, "gt": False, "lt": False, "zero": False}
    while True:
        (opcode, arguments) = code[pc]
#       For debugging:
#        stack.print()
#        for i in range(8):
#            print(f"{registerNames[i]}: {registers[i]}", end = " ")
#        print()
#        print(75*"-")
#        print(pc, ": ", opcode, arguments)

        pc += 1
        if opcode == "pushq":
            stack.push(getVal(arguments[0]))
            continue
        if opcode == "popq":
            putVal(arguments[0], stack.pop())
            continue
        if opcode == "callq" and arguments[0][0].startswith("printf"):
            print(registers[6])  # The value to be printed is in %rsi
            continue
        if opcode == "callq" and not arguments[0][0].startswith("printf"):
            stack.push(pc)
            pc = labels[arguments[0][0]]
            continue
        if opcode == "ret":
            if stack.size() == 0:  # Returning back to the OS
                return
            else:
                pc = stack.pop()
            continue
        if opcode == "movq":
            putVal(arguments[1], getVal(arguments[0]))
            continue
        if opcode == "testq":
            x = getVal(arguments[0])
            y = getVal(arguments[1])
            flags["zero"] = False
            if x & y == 0:
                flags["zero"] = True
            continue
        if opcode == "cmpq":
            x = getVal(arguments[0])
            y = getVal(arguments[1])
            flags["eq"], flags["gt"], flags["lt"] = False, False, False
            if x == y:
                flags["eq"] = True
            elif x > y:
                flags["lt"] = True
            else:
                flags["gt"] = True
            continue
        if opcode == "je":
            if flags["eq"]:
                pc = labels[arguments[0][0]]
            continue
        if opcode == "jne":
            if not flags["eq"]:
                pc = labels[arguments[0][0]]
            continue
        if opcode == "jl":
            if flags["lt"]:
                pc = labels[arguments[0][0]]
            continue
        if opcode == "jle":
            if flags["lt"] or flags["eq"]:
                pc = labels[arguments[0][0]]
            continue
        if opcode == "jg":
            if flags["gt"]:
                pc = labels[arguments[0][0]]
            continue
        if opcode == "jge":
            if flags["gt"] or flags["eq"]:
                pc = labels[arguments[0][0]]
            continue
        if opcode == "jz":
            if flags["zero"]:
                pc = labels[arguments[0][0]]
            continue
        if opcode == "jmp":
            pc = labels[arguments[0][0]]
            continue
        if opcode == "incq":
            putVal(arguments[0], getVal(arguments[0]) + 1)
            continue
        if opcode == "addq":
            putVal(arguments[1], getVal(arguments[0]) + getVal(arguments[1]))
            continue
        if opcode == "subq":
            putVal(arguments[1], getVal(arguments[1]) - getVal(arguments[0]))
            continue
        if opcode == "imulq":
            putVal(arguments[1], getVal(arguments[0]) * getVal(arguments[1]))
            continue
        if opcode == "andq":
            putVal(arguments[1], getVal(arguments[0]) & getVal(arguments[1]))
            continue
        if opcode == "cqo":
            continue
        if opcode == "idivq":
            implicit = ("%rax", False, 0)
            putVal(implicit, int(getVal(implicit) / getVal(arguments[0])))
            continue
        print(opcode)
        iError()


registerNames = \
  ["%rax", "%rbx", "%rcx", "%rdx", "%rbp", "%rsp", "%rsi", "%rdi",
   "%r8", "%r9", "%r10", "%r11", "%r12", "%r13", "%r14", "%r15"]
registers = 16 * [0]
registers[5] = 8
stack = Stack()

text = stdin.readlines()
(code, labels) = parse(text)
run(code, labels)
