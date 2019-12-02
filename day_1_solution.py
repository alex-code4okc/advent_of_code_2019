import math

def fuel_requirement_by_mass(mass):
    calculation = math.floor((mass/3))-2
    
    return calculation

def recursive_fuel_requirement_by_mass(mass):
    fuel = int(math.floor((mass/3)))-2
    print(fuel)
    if(fuel>=0):
        return fuel+recursive_fuel_requirement_by_mass(fuel)
    else:
        return 0

total = 0
with open('day_1_input.txt','rt',encoding='utf-8') as file:
    for item in file.readlines():
        total += recursive_fuel_requirement_by_mass(int(item))

print(total)

with open('day_1_solved_p2.txt','wt',encoding='utf-8') as solution:
    solution.write(str(total))

