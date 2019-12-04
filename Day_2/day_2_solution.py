instructions = []
with open('day_2_input.txt','rt',encoding='utf-8') as file:
    instructions = file.read().split(',')
# print(instructions)
#instructions = '1,10,9,3,2,0,3,1,99,4,5'.split(',')

opcodes = [int(item) for item in instructions]
original = [int(item) for item in instructions]

noun = 0
verb = 0
first_position = 0
solution_found = False
#print(opcodes)
index = 0
for pos1 in range(0,100,1):
    if(solution_found):
        break
    for pos2 in range(0,100,1):
        # if(first_position==19690720):
        #     print(f"noun: {pos1}, verb: {pos2}, position0:{first_position}")
        #     break
        opcodes = original.copy()
        index = 0

        opcodes[1] = pos1
        opcodes[2] = pos2

        while(True):
            if(opcodes[index]==99): # halt
                #print(f"noun: {pos1}, verb: {pos2}, position0: {first_position}")
                first_position = opcodes[0]
                if(first_position == 19690720):
                    solution_found = True
                    noun = pos1
                    verb = pos2

                #print(index)
                #opcodes = original.copy() # reset opcodes to the beginning for next loop
                #index = 0 # reset index to the beginning for next loop
                break
            elif(opcodes[index]==1): # add
                #print(index) 
                input1 = opcodes[opcodes[index+1]]
                input2 = opcodes[opcodes[index+2]]
                addition = input1+input2
                store1 = opcodes[index+3]
                opcodes[store1] = addition
                index += 4
                #print(f'input1: {input1}, input2: {input2}, addition: {addition}',f'Store at position:{store1}')
                #print(opcodes)
                continue
            elif(opcodes[index]==2): # multiply
                #print(index)
                input1 = opcodes[opcodes[index+1]]
                input2 = opcodes[opcodes[index+2]]
                multiplication = input1 * input2
                store1 = opcodes[index+3]
                opcodes[opcodes[index+3]] = multiplication
                index += 4
                #print(f'input1: {input1}, input2: {input2}, multiplication: {multiplication}',f'At position:{store1}')
                #print(opcodes)

print(f"noun: {noun}, verb: {verb}")
#print(opcodes)
#print(f"Length of list: {len(opcodes)}")