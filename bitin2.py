

# from os import system
# system("cls")


import turtle

# Setup
screen = turtle.Screen()
screen.setup(600, 600)
t = turtle.Turtle()
t.hideturtle()
t.speed(0)

def draw_circle(x, y, radius, color):
    t.up()
    t.goto(x, y - radius)
    t.setheading(0)
    t.color(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

def draw_rectangle(x, y, width, height, color):
    t.up()
    t.goto(x, y)
    t.setheading(0)
    t.color(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()

# Draw base (rectangle)
draw_rectangle(-50, -100, 300, 100, 'red')
draw_rectangle(-50, 100, 100, 300, 'red')


# # Draw circles
draw_circle(0, 150, 50, 'red')   # Left circle
# draw_circle(30, 100, 50, 'red')    # Right circle
# draw_circle(0, -220, 60, 'red')     # Top circle

turtle.done()
