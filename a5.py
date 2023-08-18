import turtle
num_lines = 6
line_length = 100
angle = 60
turtle.hideturtle()
turtle.color('red')
turtle.fillcolor('red')
turtle.begin_fill()

for x in range(num_lines):
    turtle.forward(line_length)
    turtle.right(angle)

turtle.end_fill()
turtle.penup()
turtle.goto(10, -110)
turtle.color('white')
turtle.write('STOP',
             font=('Arial', 25, 'normal'))
turtle.done()
