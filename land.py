# #four corners start with random vavlues (1,100)
# #the middle of the four points is the average of the four values with randint(-2,2)ish offset "x step"
# #generate random terrain
# #"plus step" average surroundings points going up and down and to both sides.
# map stay in global scope
#only value being passed are the values in teh four corners (before finding the average)
#print array and continue recursively


#written by Ellie :)

import numpy as np
from random import randint
from tkinter import *



root = Tk()
canvas = Canvas(root) 
canvas.pack(expand=1, fill="both") 
screen_width = canvas.winfo_width() 
screen_height = canvas.winfo_height() 
canvas.config(width=400, height=400) #setting a size for the canvas

size = 33
board = np.full((size,size), 00)

def print_array():
    for x in range(0,size):
        for y in range(0,size):
            print(board[y][x], end=" ")
        print()

def rand_gen(half):
    return randint(int(-half/4),int(half/4))

    

def gen_land(tl, tr, bl, br):

   
    half = int((br[1] - tl[1])/2)

    center = (tl[0] + half, tl[1] + half)
    right = (center[0] + half, center[1])
    left = (center[0] - half, center[1])
    top = (center[0], center[1] - half)
    bottom = (center[0], center[1] + half)

    tl_val = board[tl] + rand_gen(half)
    tr_val =  board[tr] + rand_gen(half)
    bl_val = board[bl] + rand_gen(half)
    br_val = board[br] + rand_gen(half)
    center_val = ((tl_val + tr_val + bl_val + br_val)/4) + rand_gen(half)

    board[center] = center_val
    board[right] = (tr_val + br_val + center_val)/3
    board[left] = (tl_val + bl_val + center_val)/3
    board[top] = (tl_val + tr_val + center_val)/3
    board[bottom] = (bl_val + br_val + center_val)/3

    if half == 1:
        return

    gen_land(tl, top, left, center) #top left box
    gen_land(top, tr, center, right) #top right box
    gen_land(left, center, bl, bottom)#bottom left box
    gen_land(center, right, bottom, br) #bottom right box

    print()


    # center_val = board[center[0]][center[1]]
    # right_val = board[right[0]][right[1]]
    # left_val = board[left[0]][left[1]]
    # top_val = board[top[0]][top[1]]
    # bottom_val = board[bottom[0]][bottom[1]]


    # middle_x = (tl[0] + tr[0])/2 #middle point bt top left and top right
    # middle_y = (tr[1] + br[1])/2 #middle point bt tr and br
    # board[int(middle_x)][int(middle_y)] = (board[tl] + board[tr] + board[bl] + board[br])/4 #center point #x step
    
    # board[int(middle_x)][tl[1]] = (board[tl] + board[tr] + ((board[tl] + board[tr] + board[bl] + board[br])/4)) / 3 #top middle #plus step
    # board[int(middle_x)][bl[1]] = (board[bl] + board[br] + ((board[tl] + board[tr] + board[bl] + board[br])/4)) / 3 #bottom midle
    # board[bl[0]][int(middle_y)] = (board[bl] + board[tl] + ((board[tl] + board[tr] + board[bl] + board[br])/4)) / 3 #middle left
    # board[br[0]][int(middle_y)] = (board[br] + board[tr] + ((board[tl] + board[tr] + board[bl] + board[br])/4)) / 3 #middle right
 
    print_array()

def get_color(val):
    if 0 < val <= 25:
        return 'blue'
    elif 25 < val <= 45:
        return 'yellow'
    elif 45 < val <= 80:
        return 'green'
    else:
        return 'white' 


def draw_grid():
    for y in range(size):
        for x in range(size):
            val = board[x][y]
            canvas.create_rectangle(x*10, y*10, x*10+10, y*10+10, fill=get_color(val), outline=get_color(val))

#assigning the four corners to the original board size
board[0][0] = randint(0,100)    #tl
board[0][size - 1]  = randint(0,100)    #tr
board[size - 1][0]= randint(0,100) #not doing values 1-100   #bl
board[size - 1][size - 1] = randint(0,100)  #br


gen_land((0,0), (size-1, 0), (0, size - 1), (size-1, size-1))

draw_grid()

root.update()
root.mainloop()

    # gen_land(tl, tr, bl, br)
    # gen_land(tl, tr, bl, br)
    # gen_land(tl, tr, bl, br)
    # gen_land(tl, tr, bl, br)
    
     # tr[0] = middle_x 
    # bl[1] = middle_y
    # br[0] = middle_x
    # br[1] = middle_y

    # gen_land(tl, tr, bl, br) #tl square

    # tl[0] = middle_x
    # br[1] = middle_y
    # bl
    # gen_land(tl, tr, bl, br) #tr square
    # gen_land(tl, tr, bl, br) #bl square
    # gen_land(tl, tr, bl, br) #br square


