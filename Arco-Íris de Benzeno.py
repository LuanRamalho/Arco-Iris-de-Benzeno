import turtle
a = turtle.Screen()
col = ['red' , 'purple' , 'blue' , 'green' , 'orange' , 'yellow']
s = turtle.Turtle()
turtle.bgcolor('black')
turtle.speed(0)

for i in range(360):
    s.pencolor(col[i%6])
    s.width(i/100+1)
    s.forward(i)
    s.left(59)

a.exitonclick()