#PyLadies Session 3 labwork. The Turtle Race

import turtle              # 1.  import the modules
import random
import time

wn = turtle.Screen()       # 2.  Create a screen
wn.bgcolor('lightblue')
wn.title('Turtle Race: Red Apple VS Orange')

apple = turtle.Turtle()    # 3.  Create two turtles
orange = turtle.Turtle()
apple.color('red')
orange.color('orange')
apple.shape('turtle')
orange.shape('turtle')

#Changes the position to facing North. 
orange.up()                # 4.  Move the turtles to their starting point
apple.up()
orange.goto(-300,20)
apple.goto(-300,-20)

time.sleep(2)

while orange.position() <= (300.00,20.00) and apple.position() <= (300.00,-20.00):
    apple.forward(random.randrange(0,200))
    orange.forward(random.randrange(0,200))
if orange.position() >= (300.00, 20.00): print('ORANGE WON!')
else: print('APPLE WON!')

wn.exitonclick()
