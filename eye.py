from asyncore import loop
import turtle
turtle.speed(5)
turtle.bgcolor("black")
for sizeI in range (0,15):
    size = sizeI*15
    for x in range (3):
        turtle.color("red")
        turtle.forward(200+size)
        turtle.right(144)
        turtle.color("blue")
        turtle.forward(200+size)
        turtle.right(144)
turtle.done()