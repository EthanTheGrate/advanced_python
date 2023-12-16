import turtle

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

turtle.speed(500)
turtle.bgcolor("black")
turtle.pensize(1)

for i in range(2):
    for i in range():
        turtle.color(colors[i % len(colors)])
        turtle.forward(10)
        turtle.left(9)
    turtle.forward(30)

turtle.done()