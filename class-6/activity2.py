import turtle

Screen = turtle.Screen()
Screen.title("Turtle Tutorial 1")
turtle.bgcolor("grey")
turtle.pencolor("white")

Screen.setup(width=800, height=600)

board = turtle.Turtle()

#Star

# First Triangle
board.forward(100)
 
board.left(120)
board.forward(100)
 
board.left(120)
board.forward(100)
 
board.penup()
board.right(150)
board.forward(50)

# Second Triangle
board.pendown()
board.right(90)
board.forward(100)
 
board.right(120)
board.forward(100)
 
board.right(120)
board.forward(100)
 
turtle.done()
