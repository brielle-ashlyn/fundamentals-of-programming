from turtle import *  # Make all the Turtle graphics functions available

tracer(0)             # Do not animate the pen
hideturtle()          # Do not show the pen

x = 0
y = 0
for n in range(100):
    setposition(x,y)
    forward(100)
    penup
    right(170)
    color('red')
    forward(100)
    pendown
    right(450)
    color('purple')
    forward(100)
    left(40)
    forward(300)
    penup
    setposition(x+1,y+1)
    pendown
    forward(10)
    left(75)
    forward(90)
    color('blue')
    begin_fill()
    
    
update()              # Refresh window
done()                # Wait for the user to close the window