import turtle
import random

points = [[-100,-100], [100,-100],[-100,100],[100,100]]

def dist(p1, p2, rat):
	return [p1[0]-((p1[0]-p2[0])*rat), p1[1]-((p1[1]-p2[1])*rat)]

def adj(a,b,l,c):
    x = l.index(a)
    y = l.index(b)
    if x == len(l)-1 and y == 0:
        return True
    elif x-y == (-1)**c:
        return True
    else:
        return False

def polygon(n, r):
    cent = [turtle.xcor(), turtle.ycor()]
    points = []
    turtle.up()
    for i in range(0, n):
        turtle.seth(0)
        turtle.right((360/n)*i)
        turtle.forward(r)
        points.append([turtle.xcor(), turtle.ycor()])
        turtle.goto(cent)
    return points

def attract1(i=100000, r=200,  n=6, rat=0.5):
    points = polygon(n, r)
    prev = random.choice(points)
    start = random.choice(points)
    for k in range(0, i):
            while True:
                    np = random.choice(points)
                    if np != prev:
                    	prev = np
                    	break
            start = dist(start, np, rat)
            turtle.goto(start[0]-1,start[1])
            turtle.down()
            turtle.forward(1)
            turtle.up()
    turtle.ht()

def attract2(i=100000, r=200, n=6, rat=0.5, tract=2):
    points = polygon(n, r)
    prev = random.choice(points)
    start = random.choice(points)
    for k in range(0, i):
            while True:
                    np = random.choice(points)
                    if not adj(np, prev, points, tract):
                    	prev = np
                    	break
            start = dist(start, np, rat)
            turtle.goto(start[0]-1,start[1])
            turtle.down()
            turtle.forward(1)
            turtle.up()
    turtle.ht()

def attract3(i=50000, r=200, n=4, rat=(0.5)):
    points = polygon(n, r)
    prev = random.choice(points)
    start = random.choice(points)
    for k in range(0, i):
            while True:
                    np = random.choice(points)
                    if np != points[(points.index(prev)+2)%3]:
                    	prev = np
                    	break
            start = dist(start, np, rat)
            turtle.goto(start[0]-1,start[1])
            turtle.down()
            turtle.forward(1)
            turtle.up()
    turtle.ht()

turtle.up()
turtle.tracer(100,0)
attract3()
