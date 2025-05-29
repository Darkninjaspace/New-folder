import turtle as t

screen = t.Screen()
mypen = t.Turtle()

click_history = []

def click(x, y):
    mypen.goto(x, y)
    click_history.append((x, y))

def fill_color(color):
    mypen.begin_fill()
    mypen.fillcolor(color)
    for i in click_history:
        mypen.goto(i[0], i[1])
    mypen.end_fill()

def choose_color():
    color = screen.textinput("Choose a color", "Enter a color name or hex code:")
    if color:
        fill_color(color)
    t.listen()  # <- Re-activate key listening

def draw_circle():
    circle_size = screen.numinput("Circle Size", "Enter the size of the circle:")
    if circle_size is None:
        return
    mypen.circle(circle_size)
    t.listen()

def draw_square():
    size = screen.numinput("Square Size", "Enter the size of the square:")
    if size is None:
        return
    for i in range(4):
        mypen.forward(size)
        mypen.right(90)
    t.listen()

def draw_rectangle():
    width = screen.numinput("Width", "Enter the width of the rectangle:")
    height = screen.numinput("Height", "Enter the height of the rectangle:")
    if width is None or height is None:
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
    t.listen()

# Initial bindings
t.listen()
screen.onclick(click)
screen.onkey(choose_color, "r")
screen.onkey(lambda: mypen.clear(), "c")
screen.onkey(draw_shape, "d")

t.mainloop()
