import turtle
turtle.bgcolor("yellow")
turtle.pensize(2.5)
turtle.speed(0.5)
color=["red","green","orange","black","blue","purple"]
for x in range(9):
    for i in color:
        turtle.color(i)
        turtle.circle(150)
        turtle.left(10)
turtle.mainloop()