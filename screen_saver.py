from tkinter import *   #importing necesary libraries
from random import randint
import random

color_options = ["lemon chiffon", "peach puff", "goldenrod", "light pink", 
"royal blue", "light sea green", "medium aquamarine", "tomato", "rosy brown",  
"honeydew2", "dark orchid", "coral", "lavender", "medium violet red", "misty rose"]  #getting a list of cute pastel colors to choose from instead of the boring ugly given colors like "magenta" and "red"

def select_color(): #creating a function to remove colors that are selectred from list so all shapes are unique colors
    color = random.choice(color_options)
    color_options.remove(color)
    return color

class Circles:    #creating a class for circles
    def __init__(self, canvas): #constructer function
        self.canvas = canvas  #initializing canvas
        self.screen_width = canvas.winfo_width() #setting the width of canvas to the screen
        self.screen_height = canvas.winfo_height() #setting the height of canvas to the screen
        self.rand_values() #initializing rand_values function
        self.create_circle() #initializing create_circles function
       
    def rand_values(self): #a function to select random values for circle size and speed
        self.radius = randint(50, 100) #select random value for radius
        self.x1_coord = randint(self.radius, self.screen_width - self.radius) #coord is within the screen from the center of circle instead of the edge
        self.y1_coord = randint(self.radius, self.screen_height - self.radius)
        self.x_speed = randint(5, 15)   #random value for speed
        self.y_speed = randint(5, 15)
        self.color = select_color()     #selecting random color from list above
        
    
    def create_circle (self): #function to create the circle
        
        x1 = self.x1_coord - self.radius #the coordinates stem from the center of the circle by adding or subtracting radius depending on the direction, x1, x2, etc.
        y1 = self.y1_coord - self.radius
        x2 = self.x1_coord + self.radius
        y2 = self.y1_coord + self.radius

        self.circle = self.canvas.create_oval(x1, y1, x2, y2, fill=self.color, outline=self.color) #using tkinter to actually create the circle and fill it with the selected colors and coords

    def move_circle(self): #function to move the circle
        self.find_boundry() #calling the function to find the boundry everytime the circle moves around the screen
        self.x1_coord += self.x_speed #moving the circle with the given random speed
        self.y1_coord += self.y_speed
        self.canvas.move(self.circle, self.x_speed, self.y_speed) #using tkinter move function to make the circle move around the screen

    def find_boundry(self): #creating the function to move the circel
        if not self.radius < self.x1_coord < self.screen_width - self.radius:
            self.x_speed = -self.x_speed #if the point radiating from the radius of the circle is not within tje bounds of the screen width, flipping the sign to make the circle move the opposite way
       
        if not self.radius < self.y1_coord < self.screen_height - self.radius:
            self.y_speed = -self.y_speed #if the point radiating from the radius of the circle is not within tje bounds of the screen height, flipping the sign to make the circle move the opposite way

class Horz_Ovals: #creating class for horz_ovals
    def __init__(self, canvas): #most of this code is copy pasted from the circles class
        self.canvas = canvas

        self.screen_width = canvas.winfo_width()
        self.screen_height = canvas.winfo_height()

        self.rand_values()
        self.create_horz_oval()
       
    def rand_values(self):
        self.radius = randint(50, 100)
        self.x1_coord = randint(self.radius, self.screen_width - self.radius) #everything im this class is the same and functions the same as the circle class except the variabels being names horz_oval instead
        self.y1_coord = randint(self.radius, self.screen_height - self.radius)
        self.x_speed = randint(5, 15)   
        self.y_speed = randint(5, 15)
        self.color = select_color()       
    
    def create_horz_oval (self):
        
        x1 = self.x1_coord - self.radius
        y1 = self.y1_coord - self.radius
        x2 = self.x1_coord + self.radius 
        y2 = self.y1_coord + self.radius

        self.horz_oval = self.canvas.create_oval(x1, y1+70, x2, y2, fill=self.color, outline=self.color) #adding val 70 to y1 is the main difference to change it from a circle to a horz oval 

    def move_horz_oval(self):
        self.find_boundry()
        self.x1_coord += self.x_speed
        self.y1_coord += self.y_speed
        self.canvas.move(self.horz_oval, self.x_speed, self.y_speed)

    def find_boundry(self): #all other notes for functions in this class can be seen in the circle class bc it is the same otherwise.
        if not self.radius < self.x1_coord < self.screen_width - self.radius:
            self.x_speed = -self.x_speed
       
        if not self.radius < self.y1_coord < self.screen_height - self.radius:
            self.y_speed = -self.y_speed

class Vert_Ovals: #class for vert ovals, copied from circle class and updated
    def __init__(self, canvas):
        self.canvas = canvas

        self.screen_width = canvas.winfo_width()
        self.screen_height = canvas.winfo_height()

        self.rand_values()
        self.create_vert_oval()
       
    def rand_values(self):
        self.radius = randint(50, 100)
        self.x1_coord = randint(self.radius, self.screen_width - self.radius)
        self.y1_coord = randint(self.radius, self.screen_height - self.radius)
        self.x_speed = randint(5, 15)   
        self.y_speed = randint(5, 15)
        self.color = select_color()      
    
    def create_vert_oval (self):
        
        x1 = self.x1_coord - self.radius
        y1 = self.y1_coord - self.radius
        x2 = self.x1_coord + self.radius 
        y2 = self.y1_coord + self.radius

        self.vert_oval = self.canvas.create_oval(x1+70, y1, x2, y2, fill=self.color, outline=self.color) #changing the x1 value by 70 to create a vert oval instead of a circle

    def move_vert_oval(self):
        self.find_boundry()
        self.x1_coord += self.x_speed
        self.y1_coord += self.y_speed
        self.canvas.move(self.vert_oval, self.x_speed, self.y_speed)

    def find_boundry(self):
        if not self.radius < self.x1_coord < self.screen_width - self.radius:
            self.x_speed = -self.x_speed
       
        if not self.radius < self.y1_coord < self.screen_height - self.radius:
            self.y_speed = -self.y_speed

class Rects: #class for rectangles, also copied from circles class
    def __init__(self, canvas):
        self.canvas = canvas
        self.screen_width = canvas.winfo_width()
        self.screen_height = canvas.winfo_height()
        self.rand_values()
        self.create_rect()
       
    def rand_values(self):
        self.radius = randint(50, 100)
        self.x1_coord = randint(self.radius, self.screen_width - self.radius) #bc this came from circles class some variables still use terms like radius, but are reffereing to the height/length of the rectangles sides instead.
        self.y1_coord = randint(self.radius, self.screen_height - self.radius)
        self.x_speed = randint(5, 15)   
        self.y_speed = randint(5, 15)
        self.color = select_color()
        
    def create_rect (self):
        x1 = self.x1_coord - self.radius
        y1 = self.y1_coord - self.radius
        x2 = self.x1_coord + self.radius
        y2 = self.y1_coord + self.radius
        self.rect = self.canvas.create_rectangle(x1+70, y1, x2, y2, fill=self.color, outline=self.color) #stretching the rect out on the x1 point so it is not a square

    def move_rect(self):
        self.find_boundry()
        self.x1_coord += self.x_speed
        self.y1_coord += self.y_speed
        self.canvas.move(self.rect, self.x_speed, self.y_speed)

    def find_boundry(self):
        if not self.radius < self.x1_coord < self.screen_width - self.radius:
            self.x_speed = -self.x_speed
       
        if not self.radius < self.y1_coord < self.screen_height - self.radius:
            self.y_speed = -self.y_speed

class Squares: #class for square 
    def __init__(self, canvas):
        self.canvas = canvas
        self.screen_width = canvas.winfo_width()
        self.screen_height = canvas.winfo_height()
        self.rand_values()
        self.create_square()
       
    def rand_values(self):
        self.radius = randint(50, 100)
        self.x1_coord = randint(self.radius, self.screen_width - self.radius)
        self.y1_coord = randint(self.radius, self.screen_height - self.radius)
        self.x_speed = randint(5, 15)   
        self.y_speed = randint(5, 15)
        self.color = select_color()
        
    def create_square (self):
        x1 = self.x1_coord - self.radius
        y1 = self.y1_coord - self.radius
        x2 = self.x1_coord + self.radius
        y2 = self.y1_coord + self.radius
        self.square = self.canvas.create_rectangle(x1, y1, x2, y2, fill=self.color, outline=self.color) #all points are the same so the sides are equal like the circle

    def move_square(self):
        self.find_boundry()
        self.x1_coord += self.x_speed
        self.y1_coord += self.y_speed
        self.canvas.move(self.square, self.x_speed, self.y_speed)

    def find_boundry(self):
        if not self.radius < self.x1_coord < self.screen_width - self.radius:
            self.x_speed = -self.x_speed
       
        if not self.radius < self.y1_coord < self.screen_height - self.radius:
            self.y_speed = -self.y_speed

class Screen: #class for Screen

    circles = [] #lists of the various shapes that will be created and then appended into the list to move around on the screen
    squares = []
    horz_ovals = []
    vert_ovals = []
    rects= []

    def __init__(self): #constructer 
        self.root = Tk()  #initializing all tkinter required functions
        self.root.attributes("-alpha", 0.7) #makes the window transparent so it overlays the current open screen, making the current screen the "background" image.
        self.canvas = Canvas(self.root) #initializing all tkinter required functions
        self.canvas.pack(expand=1, fill="both") #initializing all tkinter required functions
        self.canvas.config(width=2000, height=2000) #setting a size for the canvas
        self.root.update()

        for index in range(randint(5, 10)): #creating a loop to randomly generate between 5 and 10 random shapes
            if index % 5 == 0: 
               self.circles.append(Circles(self.canvas)) #generate circle
            elif index % 5 == 1:
                self.horz_ovals.append(Horz_Ovals(self.canvas)) #generate horz oval
            elif index % 5 == 2:
                self.squares.append(Squares(self.canvas)) #generate square
            elif index % 5 == 3:
                self.vert_ovals.append(Vert_Ovals(self.canvas)) #generate vert oval
            else:
                self.rects.append(Rects(self.canvas)) #generate rect

        self.move_shapes() #call function to move the shapes
        self.root.mainloop()   #call tkinter function to run teh loop
    
    def move_shapes(self): #function to move the shapes
        
        for circle in self.circles:
            circle.move_circle() #if circle present move circle
        for square in self.squares:
            square.move_square() #if square present move squre
        for horz_oval in self.horz_ovals:
            horz_oval.move_horz_oval() #if horz oval present move horz oval
        for vert_oval in self.vert_ovals:
            vert_oval.move_vert_oval() #if vert oval present move vert oval
        for rect in self.rects:
            rect.move_rect() #if rect present move rect

        
        self.root.after(30, self.move_shapes) #moving the shapes 
        
Screen() #calling the screen class