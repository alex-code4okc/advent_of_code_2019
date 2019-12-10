def add(prog,pointer,C,B,A): # by default will be in address mode
    # C affects arg1, B affects arg2, 
    # A affects the store position, but that can only be reference, never immediate since its a write
    arg1 = ''
    arg2 = ''
    arg3 = ''
    if(C):
        arg1 = prog[pointer+1]
        
    else:
        arg1 = prog[prog[pointer+1]]
        # if C = 0 value is reference, if C=1 value is literal
    if(B):
        arg2 = prog[pointer+2]
    else:
        arg2 = prog[prog[pointer+2]]
    
    result = arg1 + arg2
    arg3 = prog[pointer+3]
    prog[arg3] = result
    print(f"wrote ({result} at {arg3})")    
    return pointer+4 # move pointer 4 places

def multiply(prog,pointer,C,B,A):
    arg1 = ''
    arg2 = ''
    arg3 = ''
    if(C): # C = 1
        arg1 = prog[pointer+1]
    else: # C = 0
        arg1 = prog[prog[pointer+1]]
    if(B):
        arg2 = prog[pointer+2]
    else:
        arg2 = prog[prog[pointer+2]]
    
    result = arg1 * arg2
    arg3 = prog[pointer+3]
    prog[arg3] = result
    print(f"wrote ({result} at {arg3})")
    return pointer+4 # move pointer 4 places

def _input(prog,pointer,C,B,A): # write method never in immediate mode, always address mode
    # ignore A,B,C only worry about opcode and pointer
    ID = input("Please provide the ship's air conditioner ID: ")
    ID = int(ID)
    arg1 = prog[pointer+1] # find the next address
    prog[arg1] = ID # write Input ID to address
    return pointer+2 # move pointer 2 places

def output(prog,pointer,C,B,A):
    arg1 = ''
    if(C):
        arg1 = prog[pointer+1]
    else:
        arg1 = prog[prog[pointer+1]]
    print(f"Output: {arg1}")
    return pointer+2 # move pointer 2 places

def jump_false(prog,pointer,C,B,A):
    arg1 = ''
    arg2 = ''
    arg3 = ''
    if(C):
        arg1 = prog[pointer+1]
    else:
        arg1 = prog[prog[pointer+1]]
    if(B):
        arg2 = prog[pointer+2]
    else:
        arg2 = prog[prog[pointer+2]]
    
    print(f"pointer: {pointer}, jump-to: {arg2}")
    if(arg1==0):
        # need to set pointer to the value of arg2
        return arg2
    return pointer+3

def jump_true(prog,pointer,C,B,A):
    arg1 = ''
    arg2 = ''
    arg3 = ''
    print(f"pointer {pointer}")
    print(f"pointer+1 {pointer+1}")
    print(f"pointer+2 {pointer+2}")
    if(C):
        arg1 = prog[pointer+1] # literal
    else:
        arg1 = prog[prog[pointer+1]] # reference
    if(B):
        arg2 = prog[pointer+2]
    else:
        arg2 = prog[prog[pointer+2]]
    print(f"arg1 {arg1}")
    print(f"pointer: {pointer}, jump-to: {arg2}")
    if(arg1!=0):
        return arg2
    return pointer+3

def lessthan(prog,pointer,C,B,A):
    arg1 = ''
    arg2 = ''
    arg3 = ''
    if(C):
        arg1 = prog[pointer+1]
    else:
        arg1 = prog[prog[pointer+1]]
    if(B):
        arg2 = prog[pointer+2]
    else:
        arg2 = prog[prog[pointer+2]]
    
    arg3 = prog[pointer+3]
    if(arg1<arg2):
        prog[arg3] = 1
    else:
        prog[arg3] = 0

    return pointer+4

def equal(prog,pointer,C,B,A):
    arg1 = ''
    arg2 = ''
    arg3 = ''
    if(C):
        arg1 = prog[pointer+1]
    else:
        arg1 = prog[prog[pointer+1]]
    if(B):
        arg2 = prog[pointer+2]
    else:
        arg2 = prog[prog[pointer+2]]
    
    arg3 = prog[pointer+3]
    if(arg1==arg2):
        prog[arg3] = 1
    else:
        prog[arg3] = 0

    return pointer+4

opcodes = {
    '1': add,
    '2': multiply,
    '3': _input,
    '4': output,
    '5': jump_true,
    '6': jump_false,
    '7': lessthan,
    '8': equal,
}

instructions = []
with open('day_5_input.txt','rt',encoding='utf-8') as file:
    instructions = file.read().split(',') # an array of strings

prog = [int(item) for item in instructions] # an array of ints

def IntcodeMachine():
    pointer = 0 # initialize pointer
    while(prog[pointer]!= 99): # halt operation if 99 is encountered
        opcode = str(prog[pointer]) # need to convert to str for easy manipulation
        print(f"opcode: {opcode}")
        opcode = opcode.rjust(5,'0') # pad operation, if op = 111, it will be 00111
        print(f"opcode: {opcode}")
        oper = str(int(opcode[-2:]))
        C = int(opcode[2])
        B = int(opcode[1])
        A = int(opcode[0])
        pointer = opcodes[oper](prog,pointer,C,B,A)

IntcodeMachine()