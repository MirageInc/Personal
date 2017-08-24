import turtle
import math
import time
import random
import colorsys
import numpy as np
import pickle
from PIL import Image

def lorenz(tframe=0.01, a=10, b=28, c=8/3, it=1000, x0=0.0001, y0=0.0001, z0=0.0001, dcolour=2, color="Blue"):
    turtle.bgcolor("#1e1e1e")
    turtle.color(color)
    turtle.ht()
    l = []
    
    for i in range(0, it):
        
        x1 = x0+tframe*a*(y0-x0)
        y1 = y0+tframe*(x0*(b-z0)-y0)
        z1 = z0+tframe*(x0*y0-c*z0)

        x0 = x1
        y0 = y1
        z0 = z1

        l.append((x0,y0,z0))
    with open('points.txt', 'wb') as f:
        pickle.dump(l, f)
        
#        if dcolour == 2:
#            turtle.color(colorsys.hsv_to_rgb((2.0/it*i)%1.0, 1, 1))
#        if dcolour == 1:
#            turtle.color(colorsys.hsv_to_rgb(z0/50%1, z0/50%1, 1))            

#        turtle.goto(x0*10, y0*10)

def duffing(tframe=0.01, a=0.25, b=0.4, w=1, it=30000, x0=0.0001, y0=0.0001, color="Blue"):
    turtle.bgcolor("#1e1e1e")
    turtle.ht()
    turtle.color(color)
    time = 0
    
    for i in range(0, it):
        time += tframe 
        
        x1 = x0+tframe*y0
        y1 = y0+tframe*(x0-(x0**3)-a*y0+b*math.cos(w*time))

        x0 = x1
        y0 = y1

        turtle.goto(x0*100, y0*100)

def rossler(tframe=0.01, a=0.1, b=0.1, c=14, it=20000, x0=0, y0=0.0, z0=0.0, dcolour=1, color="Blue"):
    turtle.bgcolor("#1e1e1e")
    turtle.ht()
    turtle.color(color)
    turtle.penup()
    
    for i in range(0, it):
        
        x1 = x0+tframe*(-y0-z0)
        y1 = y0+tframe*(x0+a*y0)
        z1 = z0+tframe*(b+z0*(x0-c))

        x0 = x1
        y0 = y1
        z0 = z1

        if dcolour == 2:
            turtle.color(colorsys.hsv_to_rgb((2.0/it*i)%1.0, 1, 1))
        if dcolour == 1:
            turtle.color(colorsys.hsv_to_rgb(z0/50%1, z0/50%1, 1))

        turtle.goto(y0*10, z0*10-100)
        turtle.down()

def isktractor(tframe=0.01, a=-1.395, b=1.0375, c=-1.1, d=0.935,  it=3000, x0=0.01, y0=0.01):
    turtle.bgcolor("Black")
    turtle.ht()
    turtle.up()
    minx = 0
    maxx = 0
    miny = 0
    maxy = 0
    
    for i in range(0, it):
        x1 = math.sin(a*y0)+c*math.cos(a*x0)
        y1 = math.sin(b*x0)+d*math.cos(b*y0)

        percy = abs((y1-y0)/y0)

        x0 = x1
        y0 = y1

        if x0 < minx:
            minx = x0
        if x0 > maxx:
            maxx = x0
        if y0 < miny:
            miny = y0
        if y0 > maxy:
            maxy = y0
        

        sl = random.randint(0, 2)
        op = random.randint(0, 10)

        turtle.goto(x0*350, y0*350-200)
        turtle.color(colorsys.hsv_to_rgb(percy, percy%1, 1))
        turtle.dot(1)
    print(minx, maxx, miny, maxy)

def coord(floatx, floaty, xfm=[-2.0,2.0], yfm=[-2.0,2.0], xm=[0,99], ym=[0,99]): # This maps a point between the floating point range of the calculations to an integer xy coord.
    ratx = (floatx-xfm[0])/(xfm[1]-xfm[0])
    raty = (floaty-yfm[0])/(yfm[1]-xfm[0])
    return [int(ratx*(xm[1]-xm[0])), int(raty*(ym[1]-ym[0]))]

def iskmage(tframe=0.01, a=-1.395, b=1.0375, c=-1.1, d=0.935,  it=100000, x0=0.01, y0=0.01, width=5000, height=5000):
    l = np.zeros((width,height,3),dtype=np.uint8)
    count = 0
    for i in range(0, it):
        count += 1

        x1 = math.sin(a*y0)+c*math.cos(a*x0)
        y1 = math.sin(b*x0)+d*math.cos(b*y0)

        percy = abs((y1-y0)/y0)

        x0 = x1
        y0 = y1

        cxy = coord(x0, y0, [-2.0, 1.7], [-1.1, 1.5], [0, width-1], [0,height-1])

        #l[cxy[0],cxy[1]] = (count**2, count**2, count**2)
        l[cxy[0],cxy[1]] = colorsys.hsv_to_rgb((10*count)**0.5, 10, 1)

        #turtle.goto(x0*350, y0*350-200)
        #turtle.color(colorsys.hsv_to_rgb(percy, percy%1, 1))
        #turtle.dot(1)

    img = Image.fromarray(l)
    img.save("Isktractor.png")

def c(z):
        return ((7*z+2)-math.cos(math.pi*z)*(5*z+2))/4

def coltractor(start, end, step):
    count = 0
    for i in range(start, end, step):
        count += 10
        ccl = '#'+str(hex(count))[2:]
        while True:
            if len(ccl) != 7:
                ccl += '0'
            elif len(ccl) == 7:
                break
        turtle.color(ccl)
        coltract(i)

def coltract(n):
    turtle.bgcolor("#1e1e1e")
    turtle.ht()
    turtle.up()
    x = 0
    y = n

    while n != 1:
        turtle.goto(x, (y/10)-200)
        turtle.down()
        n = c(n)
        if n > y:
            x += 5
            y = n
        elif n < y:
            x -= 5
            y = n

lorenz()
