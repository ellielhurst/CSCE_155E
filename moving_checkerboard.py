from ctypes.wintypes import SIZE
import tkinter as tk
import time

root = tk.Tk()
Frame_Width = 800
Frame_Height = 800
root.geometry(f'{Frame_Width}x{Frame_Height}')
canvas = tk.Canvas(root)
canvas.pack()
canvas.config(width=Frame_Width, height=Frame_Height)
root.title("Checkerboard")

color = "black"
SIZE = 20

moving_x = 0
while True:

    canvas.delete("all")

    moving_x += 3
    for y in range(8):

        color = "white"
        if (y % 2 == 0):
            color = "black"    

        for x in range(8):
            x1 = x*SIZE + moving_x
            y1 = y*SIZE + moving_x
            x2 = x1 + SIZE 
            y2 = y1 + SIZE 
            canvas.create_rectangle([x1,y1, x2,y2], fill=color)

            if (color == "black"):
                color = "white"
            else:
                color = "black"

            # canvas.update() ((shows the array being created))
            # time.sleep(.01)

    canvas.update()
    time.sleep(.01)

root.destroy()