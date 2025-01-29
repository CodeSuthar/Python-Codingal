import turtle

screen = turtle.Screen()
screen.bgcolor('black')

pen = turtle.Turtle()
pen.speed('fastest')
pen.hideturtle()

colors = ['violet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red']

while True:
    for step in range(200):
        pen.pencolor(colors[step % len(colors)])
        pen.width(step / 100 + 1)
        pen.forward(step)
        pen.left(59)
    
    pen.right(239)

    for step in range(200, 0, -1):
        pen.pencolor('black')
        pen.width(step / 100 + 7)
        pen.forward(step)
        pen.right(59)