from turtle import *  # Make all the Turtle graphics functions available

tracer(1)             # Do not animate the pen
hideturtle()          # Do not show the pen
x = 0
y = 0

for n in range(11):
    penup()
    setposition(x,y)
    if x == 0:
        y = y + 20 
    pendown()    
    forward(200)

right(90)
v = 0
w = 200
for n in range(11):
    penup()
    setposition(v,w)   
    if w == 200:
        v = v + 20
    pendown()
    forward(200)


update()              # Refresh window
done()                # Wait for the user to close the window