from turtle import Turtle, Screen

wn = Screen()
wn.bgcolor("white")
wn.getcanvas().create_rectangle(0, 0, 100, 100,)
alex = Turtle()
tess = Turtle()
kevin = Turtle()
distance = 2
angel = 40
pen_size = 5
alex.color("red")
alex.speed(1000)

tess.color("grey")
tess.speed(1000)

kevin.color("black")
kevin.speed(1000)

for _ in range(150):
    alex.pensize(pen_size)
    tess.pensize(pen_size)
    kevin.pensize(pen_size)

    alex.forward(distance)
    alex.left(angel)

    tess.forward(distance + 2)
    tess.left(angel + 0.5)

    kevin.forward(distance + 3)
    kevin.left(angel + 1)

    pen_size += 0.5
    distance += 3





wn.exitonclick()