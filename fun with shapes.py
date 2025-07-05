import turtle
t=turtle.Turtle()
s=turtle.Screen()
s.bgcolor('blue')
for i in range(6):
    t.forward(100)
    t.right(60)
    i=i+1
t.penup()
t.left(90)
t.forward(50)
t.pendown()
t.left(90)
for i in range(3):
    t.forward(100)
    t.right(120)
    i=i+1
t.penup()
t.right(180)
t.forward(50)
t.pendown()
t.forward(150)
t.left(90)
t.forward(75)
t.left(90)
t.forward(150)
t.left(90)
t.forward(75)
turtle.done()