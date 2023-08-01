import turtle
import random
a = turtle.Turtle()
colour = ["blue","green", 'red',"orange","pink","navy blue","yellow"]
def draw_shape(num):
    angle = 360 / num
    for _ in range(num):
        a.forward(100)
        a.right(angle)
for i in range(3, 11):
    a.color(random.choice(colour))

    draw_shape(i)
turtle.mainloop()