import turtle as t

screen = t.Screen()
mypen = t.Turtle()


# This code is a simple turtle graphics program that sets up a screen and a turtle pen.
"""
THESE ARE THE COMMANDS YOU CAN USE:
mypen.penup()
mypen.pendown()
mypen.penspeed(1)
mypen.begin_fill()
mypen.end_fill()
mypen.fillcolor("red") #can also do hex color
mypen.circle(50) #draws a circle with radius 50
mypen.forward(100) #moves the turtle forward 100 units
mypen.

screen.onclick(henry)
def henry(x, y):

turtle.listen()

screen.onkey(ben,"space")
def ben():
"""

def click(x, y):
    mypen.goto(x, y)
    click_history.append((x, y))

click_history = []

def fill_color(color):
   mypen.begin_fill()
   for i in click_history:
      mypen.goto(i[0], i[1])
      mypen.fillcolor(color)
   mypen.end_fill()
   

def choose_color():
   color = screen.textinput("Choose a color", "Enter a color name or hex code:")
   if color:
      fill_color(color)
   screen.onkey(choose_color, "r")
   t.listen()


def draw_circle():
   circle_size = screen.numinput("Circle Size", "Enter the size of the circle:")
   if circle_size is None:
      t.listen()
      return
   mypen.circle(circle_size)
   t.listen()

def draw_square():
   size = screen.numinput("Square Size", "Enter the size of the square:")
   if size is None:
      t.listen()
      return
   for i in range(4):
      mypen.forward(size)
      mypen.right(90)
   t.listen()

def draw_rectangle():
   width = screen.numinput("Width", "Enter the width of the rectangle:")
   height = screen.numinput("Height", "Enter the height of the rectangle:")
   if width is None or height is None:
      t.listen()
      return
   for i in range(2):
      mypen.forward(width)
      mypen.right(90)
      mypen.forward(height)
      mypen.right(90)
   t.listen()

def draw_shape():
    shape = screen.textinput("Shape", "Enter the shape to draw (circle, square, rectangle):")
    if shape is None:
        t.listen()
        return

    shape = shape.lower()
    if shape == "circle":
        draw_circle()
    elif shape == "square":
        draw_square()
    elif shape == "rectangle":
        draw_rectangle()
    
    screen.onkey(draw_shape, "d")

t.listen()
screen.onclick(click)
screen.onkey(choose_color, "r")
screen.onkey(lambda: mypen.clear(), "c")
screen.onkey(draw_shape, "d")

t.mainloop()