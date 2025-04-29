import turtle

screen = turtle.Screen()
screen.bgcolor("lightblue")

t = turtle.Turtle()
t.pensize(3)

t.color("red", "yellow")
t.begin_fill()
for _ in range(3):
    t.forward(100)
    t.left(120)
t.end_fill()

t.penup()
t.goto(150, 0)
t.pendown()

t.color("green", "blue")
t.begin_fill()
for _ in range(4):
    t.forward(100)
    t.left(90)
t.end_fill()

t.penup()
t.goto(-150, 0)
t.pendown()

t.color("purple", "orange")
t.begin_fill()
for _ in range(6):
    t.forward(70)
    t.left(60)
t.end_fill()

t.hideturtle()
turtle.done()