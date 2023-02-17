import turtle
import numpy as np

caneta = turtle.Turtle()

def quadrado(x):
    turtle.pensize(3)
    for i in range(4):
        turtle.fd(x)
        turtle.right(90)
 
# Coloque seu código aqui:

for i in range(2, 200, 5):
    quadrado(i)

turtle.exitonclick()
turtle.bye()