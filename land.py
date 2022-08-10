# #four corners start with random vavlues (1,100)
# #the middle of the four points is the average of the four values with randint(-2,2)ish offset "x step"
# #generate random terrain
# #"plus step" average surroundings points going up and down and to both sides.
# map stay in global scope
#only value being passed are the values in teh four corners (before finding the average)
#print array and continue recursively


import colorama
from colorama import Fore 
colorama.init(autoreset=True)
import numpy as np
from random import randint
from tkinter import *



#root.attributes("-alpha", 0.7) #makes the window transparent so it overlays the current open screen, making the current screen the "background" image.
# canvas = Canvas(root) 
# canvas.pack(expand=1, fill="both") 
# canvas.config(width=2000, height=2000) #setting a size for the canvas
# root = Tk() 
# root.update()
# root.mainloop()

size = 5
board = np.full((size,size), 00)

def print_array():
    for x in range(0,size):
        for y in range(0,size):
            print(str(board[y][x]), end=" ")
        print()

def gen_land(tl, tr, bl, br):

    #hi

    middle_x = (tl[0] + tr[0])/2 #middle point bt top left and top right
    middle_y = (tr[1] + br[1])/2 #middle point bt tr and br
    board[int(middle_x)][int(middle_y)] = (board[tl] + board[tr] + board[bl] + board[br])/4 #center point #x step
    
    board[int(middle_x)][tl[1]] = (board[tl] + board[tr] + ((board[tl] + board[tr] + board[bl] + board[br])/4)) / 3 #top middle #plus step
    board[int(middle_x)][bl[1]] = (board[bl] + board[br] + ((board[tl] + board[tr] + board[bl] + board[br])/4)) / 3 #bottom midle
    board[bl[0]][int(middle_y)] = (board[bl] + board[tl] + ((board[tl] + board[tr] + board[bl] + board[br])/4)) / 3 #middle left
    board[br[0]][int(middle_y)] = (board[br] + board[tr] + ((board[tl] + board[tr] + board[bl] + board[br])/4)) / 3 #middle right
 
    print_array()



#assigning the four corners to the original board size
board[0][0] = 20  #randint(0,100)    #tl
board[0][size - 1]  = 15  #randint(0,100)    #tr
board[size - 1][0]= 5 #randint(0,100) #not doing values 1-100   #bl
board[size - 1][size - 1] = 10 #randint(0,100)  #br


gen_land((0,0), (size-1, 0), (0, size - 1), (size-1, size-1))

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


