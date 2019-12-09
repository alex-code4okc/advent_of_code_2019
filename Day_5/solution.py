instructions = []

with open('day_5_input.txt','rt',encoding='utf-8') as file:
    instructions = file.read().split(',')

opcodes = {'1':'add',
            '2':'multiply',
            '3':'input',
            '4':'output',
            '99':'halt'}

op = [int(item) for item in instructions]
original = [int(item) for item in instructions]

# pointer will increase according to what instruction was just performed
# for example: if opcode '01' is encountered, pointer moves 4 positions
# if opcode '02' is encountered, pointer moves 4 positions
# if opcode '03' is encountered, pointer moves 2 positions
# if opcode '04' is encountered, pointer moves 2 positions
# if opcode '99' is encountered, program halts
pointer = 0 
while(op[pointer] != 99):
    print(f"pointer: {pointer}")
    oper = str(op[pointer]) # initially pointer is 0
    # oper should be checked for length, if 4, it has parameter modes, otherwise it it's a normal instruction
    if(len(oper)>1): #parameterized if len is 2 or greater, Assume A,B,C are 0 unless they can be filled
        print(oper)
        A,B,C = (0,0,0)
        DE = int(oper[-2:]) # guaranteed to be at least 2 digits
        if(len(oper)==3):
            C = int(oper[-3])
        if(len(oper)==4):
            C = int(oper[-3])
            B = int(oper[-4])
        elif(len(oper)>=5):
            C = int(oper[-3])
            B = int(oper[-4])
            A = int(oper[-5])
        print(f"options: A:{A}, B:{B}, C:{C}")
        if(DE == 99):
            break
        elif(DE == 3):
            ID = input("Please provide the ship's air conditioner ID: ")
            ID = int(ID)
            # store ID at reference in position+1
            op[op[pointer+1]] = ID
            #print(f"{ID} stored at position {op[pointer+1]}")
            #increment pointer by 2
            pointer += 2
            continue
        elif(DE == 4): # output
            if(C==1): # literal value of param
                print(f"output: {op[pointer+1]}")
            elif(C==0): # reference value
                print(f"output: {op[op[pointer+1]]}")
            # increment pointer by 2
            pointer += 2
            
            continue
        elif(DE == 5):
            param = 0
            if(C==1):
                param = op[pointer+2]
            elif(C==0):
                param = op[op[pointer+2]]
            if(op[pointer+1]!=0):
                pointer = param
                continue
            else:
                pass
            pointer+=3
            continue
        elif(DE == 6):
            param = 0
            if(C==1):
                param = op[pointer+2]
            elif(C==0):
                param = op[op[pointer+2]]
            if(op[pointer+1]==0):
                pointer = param
                continue
            else:
                pass
            pointer+=3
            continue
        elif(DE == 7):
            param1 = 0
            param2 = 0
            if(C==1):
                param1 = op[pointer+1] # value
            elif(C==0):
                param1 = op[op[pointer+1]] # reference
            
            if(B==1):
                param2 = op[pointer+2] # value
            elif(B==0):
                param2 = op[op[pointer+2]] # reference
            if(param1<param2):
                op[op[pointer+3]] = 1
            else:
                op[op[pointer+3]] = 0
            pointer+=4
            continue
        elif(DE == 8):
            param1 = 0
            param2 = 0
            if(C==1):
                param1 = op[pointer+1] # value
            elif(C==0):
                param1 = op[op[pointer+1]] # reference
            
            if(B==1):
                param2 = op[pointer+2] # value
            elif(B==0):
                param2 = op[op[pointer+2]] # reference
            if(param1==param2):
                op[op[pointer+3]] = 1
            else:
                op[op[pointer+3]] = 0
            pointer+=4
            continue
        elif(DE == 1): # add 
            param1 = 0
            param2 = 0
            if(C==1):
                param1 = op[pointer+1] # value
            elif(C==0):
                param1 = op[op[pointer+1]] # reference
            
            if(B==1):
                param2 = op[pointer+2] # value
            elif(B==0):
                param2 = op[op[pointer+2]] # reference

            result = param1 + param2
            op[op[pointer+3]] = result
            # print(f"store {result} at position {op[pointer+3]}")
            pointer+=4
            continue
        elif(DE == 2): # multiply
            param1 = 0
            param2 = 0
            if(C==1):
                param1 = op[pointer+1] # value
            elif(C==0):
                param1 = op[op[pointer+1]] # reference

            if(B==1):
                param2 = op[pointer+2] # value
            elif(B==0):
                param2 = op[op[pointer+2]] # reference

            result = param1*param2
            op[op[pointer+3]] = result # reference store
            # print(f"store {result} at position {op[pointer+3]}")
            pointer+=4
            
            continue
    else: #len is not 4, instruction is without parameters modes and interpreted as referential
        if(oper == '99'):
            break
        elif(oper == '5'): # reference mode
            if(op[pointer+1]!=0):
                pointer = op[op[pointer+2]]
                continue
            else:
                pass
            pointer+=3
            continue
        elif(oper == '6'): # reference mode
            if(op[pointer+1]==0):
                pointer = op[op[pointer+2]]
                continue
            else:
                pass
            pointer+=3
            continue
        elif(oper == '7'): # reference mode
            if(op[pointer+1]<op[pointer+2]):
                op[op[pointer+3]] = 1
            else:
                op[op[pointer+3]] = 0
            pointer+=4
            continue
        elif(oper == '8'): # reference mode
            if(op[pointer+1]==op[pointer+2]):
                op[op[pointer+3]] = 1
            else:
                op[op[pointer+3]] = 0
            pointer+=4
            continue
        elif(oper == '4'):
            print(f"output: {op[op[pointer+1]]}")
            # increment pointer by 2
            pointer += 2
        elif(oper == '3'):
            print(oper)
            # request user input
            ID = input("Please provide the ship's air conditioner ID: ")
            ID = int(ID)
            op[op[pointer+1]] = ID
            #increment pointer by 2
            # print(f"store {ID} at position {op[pointer+1]}")
            pointer += 2
            
            continue
        elif(oper == '1'):
            #print(oper)
            
            param1 = op[op[pointer+1]]
            param2 = op[op[pointer+2]]
            result = param1+param2
            op[op[pointer+3]] = result
            # print(f"store {result} at position {op[pointer+3]}")
            pointer+=4
            continue
        elif(oper == '2'):
            #print(oper)
            
            param1 = op[op[pointer+1]]
            param2 = op[op[pointer+2]]
            result = param1*param2
            op[op[pointer+3]] = result
            # print(f"store {result} at position {op[pointer+3]}")
            pointer+=4
            continue

