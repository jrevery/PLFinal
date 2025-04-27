import sys

program_filepath = sys.argv[1]

program_lines =[]
with open(program_filepath, "r") as program_file:
    program_lines = [line.strip() for line in program_file.readlines()]

program = []
token_counter = 0
label_tracker = {}
for line in program_lines:
    parts = line.split(" ")
    opcode = parts[0]

    if opcode == "":
        continue
    #similar to video but I changed to SECTION rather than : ending
    if opcode == "SECTION":
        label_tracker[parts[1]] = token_counter
        continue

    program.append(opcode)
    token_counter += 1

    #from video
    if opcode == "PUSH":
        number = int(parts[1])
        program.append(number)
        token_counter += 1
    elif opcode == "PRINT":
        string_literal = ' '.join(parts[1:])
        program.append(string_literal)
        token_counter += 1
    elif opcode == "JUMPEQ0":
        label = parts[1]
        program.append(label)
        token_counter += 1
    elif opcode == "JUMPGT0":
        label = parts[1]
        program.append(label)
        token_counter += 1
    elif opcode == "JUMPLT0":
        label = parts[1]
        program.append(label)
        token_counter += 1
    elif opcode == "JUMP":
        label = parts[1]
        program.append(label)
        token_counter += 1
    #changed to accept non-number input
    elif opcode == "READ":
        data_type = parts[1]
        program.append(data_type)
        token_counter += 1
    #for string inversion
    elif opcode =="PRINTINLINE":
        string_literal = ' '.join(parts[1:])
        program.append(string_literal)
        token_counter += 1
    elif opcode == "STORE":
        store_num = parts[1]
        program.append(store_num)
        token_counter += 1
    elif opcode == "UNSTORE":
        store_num = parts[1]
        program.append(store_num)
        token_counter += 1
    
class Stack:
    #from video
    def __init__(self, size):
        self.buf = [0 for _ in range(size)]
        self.sp = -1
    
    def push(self, number):
        self.sp +=1
        self.buf[self.sp] = number

    def pop(self):
        number = self.buf[self.sp]
        self.sp -=1
        return number
    
    def top(self):
        return self.buf[self.sp]
    
stack = Stack(256)
pc = 0
#mimics 4 registers for storage
store = [0,0,0,0]

while program[pc] != "STOP":
    opcode = program[pc]
    pc += 1
    #for debug
    #print("top", stack.top())
    #from video
    if opcode == "PUSH":
        number = program[pc]
        pc += 1
        stack.push(number)

    if opcode == "POP":
        stack.pop()

    elif opcode == "ADD":
        a = stack.pop()
        b = stack.pop()
        stack.push(a+b)

    elif opcode == "SUB":
        a = stack.pop()
        b = stack.pop()
        stack.push (b-a)

    #changed to allow for printing the top element of the stack
    elif opcode == "PRINT":
        string_literal = program[pc]
        pc += 1
        if string_literal == "/top":
            print(str(stack.top()))
        else:
            print(string_literal)

    #changed to handle text or numbers
    elif opcode == "READ":
        data_type = program[pc]
        pc += 1
        value = input()
        if data_type == "NUM":
            value = int(value)
        if data_type == "TEXT":
            value = str(value)
        stack.push(value)

    elif opcode == "JUMPEQ0":
        number = stack.top()
        if number == 0:
            pc = label_tracker[program[pc]]
        else:
            pc += 1
    elif opcode == "JUMPGT0":
        number = stack.top()
        if number > 0:
            pc = label_tracker[program[pc]]
        else:
            pc += 1

    elif opcode == "JUMPLT0":
        number = stack.top()
        if number < 0:
            pc = label_tracker[program[pc]]
        else:
            pc += 1

    elif opcode == "JUMP":
        pc = label_tracker[program[pc]]
    #from me
    #saves the top element of the stack onto a separate storage location
    elif opcode == "STORE":
        store_num = int(program[pc]) - 1
        pc += 1
        store[store_num] = int(stack.pop())
    #puts data in storage back onto stack
    elif opcode == "UNSTORE":
        store_num = int(program[pc]) -1
        pc += 1
        stack.push(store[store_num])
        store[store_num] = 0

    #puts the top element of the stack back onto the stack
    elif opcode == "DUPLICATE":
        number = stack.top()
        stack.push(number)

    #prints inline, used for string flipping
    elif opcode == "PRINTINLINE":
        string_literal = program[pc]
        pc += 1
        if string_literal == "/top":
            print(str(stack.top()), end="")
        else:
            print(string_literal, end="")
    
    #converts a string into a list of characters, pushed onto the stack
    elif opcode =="CHARCONVERT":
        to_flip = str(stack.pop())
        for char in to_flip:
            stack.push(char)

    #pushes the length of a string to the stack
    elif opcode =="STRLEN":
        num = len(str(stack.top()))
        stack.push(num)


