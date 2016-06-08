from turtle import *  # Make all the Turtle graphics functions available

tracer(0)             # Do not animate the pen
hideturtle()          # Do not show the pen

setposition(0,0)
for n in range(5):
    forward(300)
    right(144)


update()              # Refresh window
done()                # Wait for the user to close the window