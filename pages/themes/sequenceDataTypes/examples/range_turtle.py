import turtle

window = turtle.Screen()
leo = turtle.Turtle()

for i in range(20):
    leo.forward(10*i)
    leo.left(90)

window.exitonclick()
