#!/usr/bin/env python
# coding: utf-8

#Circle drawing turtles 
#Created by erika % Lumi

import turtle
import random
import time



def drawSquare(t, sz):
    """Make turtle t draw a square of sz."""

    for i in range(4):
        t.forward(sz)
        t.left(90)


def drawTriangle(t, sz):
    """ Draw a tringle with equal sides """

    for i in range(3):
    	t.forward(sz)
    	t.left(120)	


def drawOctagon(t, sz):
    """ Draw a octagon with equal sides """

    for i in range(8):
    	t.forward(sz)
    	t.left(45)	


def drawStepcircle(t, sz):
    """ Draw a circle with equal sides """

    for i in range(180):
    	t.forward(sz)
    	t.left(2)	


def drawPolygon(t, sideLength, numSides, left):
    turnAngle = 360 / numSides
    for i in range(numSides):
        t.forward(sideLength)
        if left:
	        t.left(turnAngle)
        else:
	    	t.right(turnAngle)


def drawCircle(t, radius, left, fillcolor):
#    t.up()
    if left:
    	t.goto(t.xcor(), t.ycor()-radius)
    else:
    	t.goto(t.xcor(), t.ycor()+radius)
#    t.down()
#    t.pencolor(fillcolor)
    t.fillcolor(fillcolor)
    t.begin_fill()
    circumference = 2 * 3.1415 * radius
    sideLength = circumference / 360
    drawPolygon(t, sideLength, 360, left)
    t.end_fill()



def createTurtle(name, color, position, speed):
	t = turtle.Turtle()
	t.color(color)
	t.shape('turtle')
	t.up()
	t.speed(speed)
	t.goto(position)
	t.down()
	t.name = name
	return t


wn = turtle.Screen()
wn.bgcolor('black')

t = createTurtle("Ada", "pink", (0,0), 50)

drawCircle(t, 50, False, "blue")
drawCircle(t, 40, True, "green")


time.sleep(2)