import turtle
import random

def dist(a,b):
	return ((a[0]-b[0])**2+(a[1]-b[1])**2)**0.5

def manh(a,b):
    return (abs(a[0]-b[0])+abs(a[1]-b[1]))

def closest(l, n):
    copy = [l[i] for i in range(0, len(l))]
    nl = []
    for i in range(0, n):
        nl.append(l.index(min(copy)))
        del copy[copy.index(min(copy))]
    return nl

def voronoi(width=1000, height=1000, points=30, epsilon=0.1, closen=6):
    l = [[[random.randint(-(width/2), (width/2)),random.randint(-(height/2), (height/2))],[random.uniform(0,1),random.uniform(0,1),random.uniform(0,1)]] for i in range(points)]
    for y in range(-int(width/2), int(width/2)):
        for x in range(-int(height/2), int(height/2)):
            colour = 'white'
            dista = 10000
            distl = []
            for k in range(0, len(l)):
                distl.append(manh((x,y),l[k][0]))
            for i in closest(distl, closen):
                a = manh((x,y),l[i][0])
                if a <= (dista+epsilon) and a >= (dista-epsilon):
                    colour = 'white'
                    break
                elif a < dista:
                    colour = l[i][1]
                    dista = a
            turtle.up()
            turtle.goto(x-1,y)
            turtle.down()
            turtle.color(colour)
            turtle.forward(1)

turtle.tracer(0,0)
voronoi()
turtle.update()