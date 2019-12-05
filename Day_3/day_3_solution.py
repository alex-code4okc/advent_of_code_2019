import math, operator

DASH = '-' # wire1 = 
BAR = '|'
HIT = 'X'
CORNER = '+'

wire1_map = {DASH: '-',BAR:'|'}
wire2_map = {DASH: '=',BAR:'/'}

wires = []
with open('day_3_input.txt','rt',encoding='utf-8') as file:
    wires = file.readlines()

wire1 = wires[0].replace('\n','') # removing new line character
wire2 = wires[1].replace('\n','')

wire1_movements = wire1.split(',') # turning into an array of instructions
wire2_movements = wire2.split(',')

# assuming a position of 0 on a cartesian grid

start_x = 0
start_y = 0
start = (start_x,start_y)

def path_generator(movements,path,full_path,start_point):
    '''Caculates a list of paths based on movement isntructions and a starting point of (0,0)'''
    path.append(start_point)
    for instruction in movements:
        operation = instruction[0]
        move = int(instruction[1:])
        if(operation=='L'):
            last_point = path[-1]
            full_path.append(last_point) # might add same point twice, eliminating move+1 in the range would fix this
            
            for left in range(last_point[0],move+1,1):
                full_path.append( (last_point[0] - left, last_point[1]) ) # y is fixed x is moving left
            new_point = (last_point[0]-move,last_point[1])
            path.append(new_point)
        elif(operation=='R'):
            last_point = path[-1]
            full_path.append(last_point)

            for right in range(last_point[0],move+1,1):
                full_path.append( (last_point[0]+right, last_point[1]) )
            new_point = (last_point[0]+move,last_point[1])
            path.append(new_point)
        elif(operation=='U'):
            last_point = path[-1]
            full_path.append(last_point)

            for up in range(last_point[1],move+1,1):
                full_path.append( (last_point[0],last_point[1]+up) )
            new_point = (last_point[0],last_point[1]+move)
            path.append(new_point)
        elif(operation=='D'):
            last_point = path[-1]
            full_path.append(last_point)

            for down in range(last_point[1],move+1,1):
                full_path.append( (last_point[0],last_point[1]-down) )
            new_point = (last_point[0],last_point[1]-move)
            path.append(new_point)
    
    return (path, full_path)

wire1_path, wire1_full_path = path_generator(wire1_movements,[],[],start)
wire2_path, wire2_full_path = path_generator(wire2_movements,[],[],start)

# shared = []

# for path in wire1_full_path:
#     if path in wire2_full_path:
#         shared.append(path)

# print(shared)

#print(wire1_full_path)

wire1_max_p = list(map(max, zip(*wire1_path))) 
wire1_min_p = list(map(min, zip(*wire1_path))) 

wire2_max_p= list(map(max, zip(*wire2_path))) 
wire2_min_p = list(map(min, zip(*wire2_path)))

x_max = max(wire1_max_p[0],wire2_max_p[0])
y_max = max(wire1_max_p[1],wire2_max_p[1])

x_min = min(wire1_min_p[0],wire2_min_p[0])
y_min = min(wire1_min_p[1],wire2_min_p[1])

print(f"x_max: {x_max},y_max: {y_max} ")
print(f"Wire1 max point: {wire1_max_p} and min point {wire1_min_p}")
print(f"Wire2 max point: {wire2_max_p} and min point {wire2_min_p}")

grid_size = max(x_max,y_max)*2 # rounding up to 14500 to avoid off by 1 errors

# print(grid_size)
# can now create a 'grid' array of known size n x n with x=0, y=0 in the middle
# for example, if x_max = 9385 and x_min = -5571, the absolute value of their distance is 14956 ~ 15000 and halfwaay point is 7500
# if y_max = 3976, and y_min = -8827, the absolute value of their distance is 12803 of those 2 take the larger
# and create n by n grid
Grid = []

def initialize_grid(grid,grid_size):
    row = []
    for x in range(0,grid_size+1):
        row.append('.')
    for x in range(0,grid_size+1):
        grid.append(row.copy())

initialize_grid(Grid,grid_size)

# mark the starting point in grid

s_point = math.floor(grid_size/2)
grid_starting_point = (s_point,s_point)

Grid[grid_starting_point[0]][grid_starting_point[0]] = 'o' # starting point

print(grid_starting_point)
print(Grid[grid_starting_point[0]][grid_starting_point[0]])

def save_grid(grid):
    with open('day_3_grid.txt','wt',encoding='utf-8') as file:
        for row in grid:
            for symbol in row:
                file.write(symbol)
            file.write('\n')

#save_grid(Grid)

common = [(973, -5186), (-1378, -6402), (-46, -5668), (-494, -6012), (-3326, -3480), (-3127, -3024), (-3365, -3448), (-1366, -6590), (-1378, -6307), (499, -6895), (-3946, -3448), (39, -5668), (-377, -6012), (-1378, -6560), (-4221, -3448), (1421, -6026), (974, -6355), (-4221, -3429), (-2367, -4101), (-4114, -3611), (-2246, -3164), (1913, -6258), (973, -5348), (-2326, -3210), (-3749, -3403), (996, -7017), (-3749, -3611), (-3266, -3024), (562, -5065), (-2183, -4106), (-3480, -2559), (-524, -6012), (-3365, -3024), (-3749, -3480), (562, -4757), (-4099, -3660), (499, -6750), (-4083, -3809), (-821, -6254), (-455, -6012), (-3852, -2559)]

def write_path_to_grid(grid,start,movements,collisions,sym1,sym2,fpath,sdistance):
    path = []
    path.append(start)
    fpath.append(start)
    steps = 0
    for instruction in movements:
        operation = instruction[0]
        move = int(instruction[1:])
        #print(f"operation: {operation}, move: {move}")
        if(operation=='L'):
            last_point = path[-1]
            for left in range(1,move+1,1): # length is still move (shifted by 1)
                steps+=1
                x = last_point[0]-left
                y = last_point[1]
                if((x,y) in common and (x,y) not in sdistance):
                    sdistance[(x,y)] = steps
                fpath.append((x,y))
                #print((x,y))
                if(left == move):
                    grid[x][y] = CORNER # corner write +, assuming wires don't cross at +
                    # print(f'({x},{y}): +')
                else:
                    if(grid[x][y] == sym2[DASH]):
                        # grid already contains '-' write 'X' and capture collision point
                        grid[x][y] = HIT
                        collisions.append((x,y) )
                    else:
                        grid[x][y] = sym1[DASH] # L movement write a dash 
            new_point = (last_point[0]-move,last_point[1])
            path.append(new_point)
        elif(operation=='R'):
            last_point = path[-1]
            for right in range(1,move+1,1): # starts 1 ahead of starting x
                steps+=1
                x = last_point[0]+right
                y = last_point[1]
                if((x,y) in common and (x,y) not in sdistance):
                    sdistance[(x,y)] = steps
                #print((x,y))
                fpath.append((x,y))
                if(right == move):
                    grid[x][y] = CORNER # corner write + 
                    # print(f'({x},{y}): +')
                else:
                    if(grid[x][y] == sym2[DASH]):
                        # grid already contains '-' write 'X' and capture collision point
                        grid[x][y] = HIT
                        collisions.append((x,y))
                    else:
                        grid[x][y] = sym1[DASH] # R movement write a dash 
            new_point = (last_point[0]+move,last_point[1])
            path.append(new_point)
        elif(operation=='U'):
            last_point = path[-1]
            for up in range(1,move+1,1):
                steps+=1
                x = last_point[0]
                y = last_point[1]+up
                if((x,y) in common and (x,y) not in sdistance):
                    sdistance[(x,y)] = steps
                #print((x,y))
                fpath.append((x,y))
                if(up == move):
                    grid[x][y] = CORNER # corner write + 
                    # print(f'({x},{y}): +')
                else:
                    if(grid[x][y]== sym2[BAR]):
                        # grid already contains '|' write 'X' and capture collision point
                        grid[x][y] = HIT
                        collisions.append((x,y))
                    else:
                        grid[x][y] = sym1[BAR] # U movement write a dash 
            new_point = (last_point[0],last_point[1]+move)
            path.append(new_point)
        elif(instruction[0]=='D'):
            last_point = path[-1]
            for down in range(1,move+1,1):
                steps+=1
                x = last_point[0]
                y = last_point[1]-down
                if((x,y) in common and (x,y) not in sdistance):
                    sdistance[(x,y)] = steps
                #print((x,y))
                fpath.append((x,y))
                if(down == move):
                    grid[x][y] = CORNER # corner write +
                    # print(f'({x},{y}): +')
                else:
                    if(grid[x][y] == sym2[BAR]):
                        # grid already contains '|' write 'X' and capture collision point
                        grid[x][y] = HIT
                        collisions.append( (x,y) )
                    else:
                        grid[x][y] = sym1[BAR] # D movement write a dash 
            new_point = (last_point[0],last_point[1]-move)
            path.append(new_point)
    #print(path)

    return path#collisions

collisions = []

w1 = []
w2 = []
p1_d = {}
p2_d = {}
write_path_to_grid(Grid,(0,0),wire1_movements,collisions,wire1_map,wire2_map,w1,p1_d)

write_path_to_grid(Grid,(0,0),wire2_movements,collisions,wire2_map,wire1_map,w2,p2_d)

w1.remove((0,0))
w2.remove((0,0))
s_w1 = set(w1)
s_w2 = set(w2)

shared = []

for point in s_w1:
    if(point in s_w2):
        shared.append(point)

def manhattan_distance(start,finish):
    delta_x = finish[0] - start[0]
    delta_y = finish[1] - start[1]

    return abs(delta_x)+abs(delta_y)

distances = []
for point in shared:
    distances.append(manhattan_distance((0,0),point))

print(min(distances))
print(p1_d)
print(p2_d)

min_distance = {}
for point in shared:
   min_distance[point] = p1_d[point]+p2_d[point]

print(min_distance)
sorted_d = sorted(min_distance.items(),key=operator.itemgetter(1) )

print(sorted_d)
# save_grid(Grid)

# print(len(Grid),len(Grid[0]))

# print(wire1_max_p in wire1_path,wire1_min_p in wire1_path) # these points are not actually in the arrays
# print(wire2_max_p in wire2_path,wire2_min_p in wire2_path) # they are the max in x,y and min in x,y
# print(f"x distance: {x_distance}, y distance: {y_distance}")
