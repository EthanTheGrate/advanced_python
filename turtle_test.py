import turtle

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

turtle.speed(500)
turtle.bgcolor("black")
turtle.pensize(1)

for i in range(1000):
    turtle.color(colors[i % len(colors)])
    turtle.forward(35)
    turtle.left(13)

turtle.done()