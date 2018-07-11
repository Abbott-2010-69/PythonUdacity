import turtle
def draw_octagon(some_turtle):
    for i in range(1,9):
        some_turtle.forward(100)
        some_turtle.right(45)


def draw_pentagram(some_turtle):
    for i in range(1,6):
        some_turtle.forward(100) #1
        some_turtle.left(72) #2
        some_turtle.forward(100) #3
        some_turtle.right(144) #4

def draw_pentagon(some_turtle):
    for i in range(1,6):
        some_turtle.forward(100)
        some_turtle.right(72)


def draw_hexagon(some_turtle):
    for i in range(1, 7):
        some_turtle.forward(100)
        some_turtle.right(60)

def draw_circle(some_turtle):
    some_turtle.circle(100)

def draw_triangle(some_turtle):
    for i in range(1,4):
        some_turtle.forward(100)
        some_turtle.right(120)

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_shape():

    window = turtle.Screen()
    window.bgcolor("red")
    mover = turtle.Turtle()
    mover.shape("turtle")
    mover.color("yellow")

    for i in range(1,37):
        #draw_square(mover)
        #draw_triangle(mover)
        #draw_circle(mover)
        #draw_hexagon(mover)
        #draw_pentagon(mover)
        #draw_pentagram(mover)
        draw_octagon(mover)
        mover.right(10)
    window.exitonclick()
draw_shape()