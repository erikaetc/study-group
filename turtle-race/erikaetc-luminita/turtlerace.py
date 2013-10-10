#Turtle race created by erikaetc & luminita

import turtle              # 1.  import the modules
import random

wn = turtle.Screen()       # 2.  Create a screen
wn.bgcolor('black')

lance = turtle.Turtle()    # 3.  Create two turtles
lance.color('red')
lance.shape('turtle')

andy = turtle.Turtle()
andy.color('blue')
andy.shape('turtle')

andy.up()                  # 4.  Move the turtles to their starting point
lance.up()
andy.goto(-290,-80)
lance.goto(-290,-40)


while lance.xcor() <= 250 and andy.xcor() <= 250:
	print "Lance's position:" + " " + str(lance.xcor()) + ", Andy's position:" + " " + str(andy.xcor())

	l = random.randrange(1,20)
	lance.forward(l)

	a = random.randrange(1,20)
	andy.forward(a)

print "Lance's finishing position:" + " " + str(lance.xcor()) + ", Andy's finishing position:" + " " + str(andy.xcor())

if lance.xcor() > andy.xcor():
	print ("Lance won!")
	lance.turtlesize(3, 3, 3)

elif andy.xcor() > lance.xcor():
	print ("Andy won!")
	andy.turtlesize(3, 3, 3)

else:
	print ("It's a draw!")


wn.exitonclick()
