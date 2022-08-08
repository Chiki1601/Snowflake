import snowflake

s=snowflake.snowflake()

def mySnowflake():
    snow.drawbranch(60)
    snow.drawbranch(60)
    snow.drawbranch(60)# Multi-color Snowflake Turtle

import turtle

# Assign a name to your turtle
snow = turtle.Turtle()
snow.shape("turtle")

colors = ["blue", "red", "yellow", "green"]

# Declare the function, snowflake
def snowflake(size, pensize, x, y):
    # turtle.pen(pensize=10)
    snow.penup()
    snow.goto(x, y)
    snow.forward(10*size)
    snow.left(45)
    snow.pendown()
    for color in colors:
        snow.color(color)

    for i in range(8):
        branch(size)
        snow.left(45)

# Create the branches
def branch(size):
    for i in range(3):
        for i in range(3):
            snow.forward(10.0*size/3)
            snow.backward(10.0*size/3)
            snow.right(45)
        snow.left(90)
        snow.backward(10.0*size/3)
        snow.left(45)
    snow.right(90)
    snow.forward(10.0*size)


snowflake(8, 6, 0, 0)

snow.pencolor("blue")
snow.goto(-100,100)
mySnowflake()

snow.goto(100,-100)
mySnowflake()
