import turtle
import time
import math


arrow=turtle.Turtle()
arrow.speed(1000)
i=10
arrow.color("blue","purple")
for i in range(1000):
    arrow.forward(50)
    for i in range(30):
        arrow.right(10)
        arrow.forward(20)
        arrow.right(i&2)
    for i in range(30):
        arrow.left(30)
        arrow.forward(20)


    arrow.right(math.sin(i+2))
    i+50
