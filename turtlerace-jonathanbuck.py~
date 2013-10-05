import turtle              # 1.  import the modules
import random
wn = turtle.Screen()       # 2.  Create a screen
wn.bgcolor('lightblue')

lance = turtle.Turtle()    # 3.  Create two turtles
andy = turtle.Turtle()
lance.color('red')
andy.color('blue')
lance.shape('turtle')
andy.shape('turtle')

andy.up()                  # 4.  Move the turtles to their starting point
lance.up()
andy.goto(-200,20)
lance.goto(-200,-20)

# your code goes here
while andy.xcor() < 200 and lance.xcor() < 200:
    andy.forward(random.randrange(1,10))
    lance.forward(random.randrange(1,10))

wn.exitonclick()

