import turtle
import random

turtle.colormode(255)


def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colour = (r, g, b)
    return random_colour


directions = [0, 90, 180, 270]
a = turtle.Turtle()
a.pensize(15)
a.speed("fastest")
a.shape("turtle")

for _ in range(100):
    a.color(random_colour())
    a.forward(30)
    a.setheading(random.choice(directions))
turtle.mainloop()