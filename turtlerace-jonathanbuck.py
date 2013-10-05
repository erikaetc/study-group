import turtle              # 1.  import the modules
import random
wn = turtle.Screen()       # 2.  Create a screen
wn.bgcolor('lightblue')

edge = wn.window_width()/2

lance = turtle.Turtle()    # 3.  Create two turtles
andy = turtle.Turtle()
lance.color('red')
andy.color('blue')
lance.shape('turtle')
andy.shape('turtle')

andy.up()                  # 4.  Move the turtles to their starting point
lance.up()
andy.goto(-edge,20)
lance.goto(-edge,-20)

# your code goes here
while andy.xcor() < edge and lance.xcor() < edge:
    andy.forward(random.randrange(1,10))
    lance.forward(random.randrange(1,10))

wn.exitonclick()

