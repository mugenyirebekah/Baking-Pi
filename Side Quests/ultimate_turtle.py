import turtle
scr = turtle.Screen()


def cube():
    turtle.pendown()
    turtle.right(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.right(150)
    turtle.forward(30)
    turtle.right(30)
    turtle.forward(50)
    turtle.right(150)
    turtle.forward(30)
    turtle.penup()



cube()

turtle.exitonclick()