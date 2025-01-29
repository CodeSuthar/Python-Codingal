import turtle

Screen = turtle.Screen()
Screen.title("Turtle Tutorial 1")
turtle.bgcolor("grey")
turtle.pencolor("white")

Screen.setup(width=800, height=600)

board = turtle.Turtle()

for i in range(8):
    board.forward(100)
    board.right(90)
    i = i + 1