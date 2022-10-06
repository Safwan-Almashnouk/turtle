from asyncore import loop
import turtle
turtle.speed(5)
turtle.bgcolor("black")
for sizeI in range (0,30):
    size = sizeI*15
    for x in range(50):
        turtle.color("white")
        turtle.circle(10)
        turtle.circle(15)
            