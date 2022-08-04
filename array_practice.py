import random

size =int(input('Enter a size: '))
rows = cols = size


#generate 2d array
graphic = []

'''
for i in range(cols):
    row = []
    for j in range(rows):
        row.append(0)
    graphic.append(row)
''' #comenting it out

graphic = [[0 for i in range(cols)] for j in range(rows)] #same as above = 2D array

for i in range(0, rows):
    for j in range(0, cols):
        graphic[i][j] = random.randint(0,2)



def print_array(arr):
    for i in range(0, rows):
        for j in range(0, cols):
            if(arr[i][i] == 1):
                print('#',end='') 
            elif(arr[i][j] == 2):
                print('.',end='')
            else:
                print('$',end='')
                
        print()

print_array(graphic)

