import turtle
from configure_screen import position_screen

t = turtle.Turtle('turtle')
position_screen(t)

t.width(4)
t.speed (500)
t.color('#4689BC')

t.penup()
t.goto(-450, 0)
t.pendown()


# Cuadrado
for vuelta in range(4):
    t.forward(100)
    t.left(90)


t.penup()
t.goto(-200, 0)
t.pendown()


# Escalera
for vuelta in range(4):
    t.left(90)
    t.forward(100)
    t.right(90)
    t.forward(100)



t.penup()
t.goto(-450, -200)
t.pendown()


# Pinchos
for vuelta in range(4):
    t.left(90)
    t.forward(100)
    t.left(180)
    t.forward(100)
    t.left(90)
    t.forward(100)


t.penup()
t.setheading(0)
t.forward(50)
t.pendown()


# Pinchos extended
# Hacer de al menos 2 formas diferentes
t.forward(100)
for vuelta in range(4):
    t.left(90)
    t.forward(100)
    t.left(180)
    t.forward(100)
    t.left(90)
    t.forward(100)


t.hideturtle()
turtle.exitonclick()
