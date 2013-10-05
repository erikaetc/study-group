## Liga's solution to turtle race 
## 

import turtle              # 1.  import the modules
import random
wn = turtle.Screen()       # 2.  Create a screen
wn.bgcolor('lightblue')

lance = turtle.Turtle()    # 3.  Create two turtles
andy = turtle.Turtle()
lance.color('blue')
andy.color('red')
lance.shape('turtle')
andy.shape('turtle')

andy.up()                  # 4.  Move the turtles to their starting point
lance.up()
andy.goto(-100,20)
lance.goto(-100,-20)

for i in range(70):			#5.  Turtles competing by moving 70 times for a random distance
	andy.forward(random.randrange(1,10))
	lance.forward(random.randrange(1,10))
if andy.xcor() > lance.xcor():		#6.  Check which turtle won and make winner draw a finish line
	wn.title("Andy won")
	x = andy.pos()
	andy.left(90)
	andy.pendown()
	andy.forward(100)
	andy.left(180)
	andy.forward(200)
	andy.left(90)
	andy.goto(x)
else:
	wn.title("Lance won")
	x = lance.pos()
	lance.left(90)
	lance.pendown()
	lance.forward(100)
	lance.left(180)
	lance.forward(200)
	lance.left(90)
	lance.goto(x)
	
wn.exitonclick()
