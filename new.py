import turtle
a = turtle.Turtle()
#a.shape("turtle")
#a.color("red")
a.color("blue")
a.shape("turtle")
for _ in range(14):
    a.backward(10)
    a.penup()
    a.backward(10)
    a.pendown()
