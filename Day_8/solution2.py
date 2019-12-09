import sys

image = ''
with open('day_8_input.txt','rt',encoding='utf-8') as file:
    image = file.read()

width = 25
height = 6
layer_size = width*height
image_size = len(image)

layers = int(image_size/layer_size)

collection = {}
layer_count = 0
layer = []

for x in range(0,image_size+1,width):
    if(x%layer_size == 0): # make a new layer
        layer_count +=1 # keep track of layers, layers are 1 indexed
        if(layer_count == 101):
            break
        layer = [] # time for a new layer
        collection['layer'+str(layer_count)] = layer
    layer.append(image[x:x+width])

# print(collection)
#### PART TWO ####
message = {}
row_indices = []

for key,layer in collection.items():
    r = 0
    for row in layer:
        for index,pixel in enumerate(row):
            if(pixel == '0' or pixel == '1'):
                if((r,index) not in row_indices):
                    row_indices.append((r,index))
                    message[(r,index)] = pixel
        r += 1

def compose_message(message,width,height):
    for y in range(0,height,1):
        row = ''
        for x in range(0,width,1):
            if( (y,x) in message):
                row += message[(y,x)]
            else:
                row += '2'
        print(row)

compose_message(message,width,height)

#### PART ONE ####
# zero_count = {}
# layer_count = 0
# zeros = 0
# for key, layer in collection.items():
#     for row in layer:
#         zeros += row.count('0')
#     zero_count[key] = zeros
#     zeros = 0

# min_zero_count_key = ''
# min_zero_count_value = sys.maxsize
# for key, count in zero_count.items():
#     if(count<min_zero_count_value):
#         min_zero_count_key = key
#         min_zero_count_value = count

# print(f"key: {min_zero_count_key}, count: {min_zero_count_value}")

# ones = 0
# twos = 0
# for row in collection[min_zero_count_key]:
#     ones += row.count('1')
#     twos += row.count('2')

# print(f"ones: {ones}")
# print(f"twos: {twos}")
# print(f"answer: {ones*twos}")



