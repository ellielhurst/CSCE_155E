import tkinter as tk
import time
import math

root = tk.Tk()
canvas = tk.Canvas(root)
canvas.pack()
root.title('Sin')
color = 'green'

for x in range(1,400):

    canvas.delete("all")
    canvas.create_rectangle([x, math.sin(x/20)*50+100, 
                        x+20, math.sin(x/20)*50+20+100], fill=color)

    canvas.update();
    time.sleep(.01)

root.destroy()
