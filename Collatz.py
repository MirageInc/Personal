import math
import turtle
import functools
import colorsys

def collatz(z): # Prints out the sequence tending to 0.
    c = 0
    print(z)
    while z != 1:
        c += 1
        print('|')
        if z%2 == 0:
            z = z/2
            print(int(z))
        elif z%2 != 0:
            z = 3*z + 1
            print(int(z))
    print(str(c)+' was the number of iterations.')

def ccollatz(z): # Returns the number of iterations it takes to get to 0.
    c = 0
    print(z)
    while z != 1:
        c += 1
        if z%2 == 0:
            z = z/2
        elif z%2 != 0:
            z = 3*z + 1
    print(c)

@functools.lru_cache(maxsize=None)
def c(z): # This performs a single iteration of the 'Collatz function'.
        return ((7*z+2)-math.cos(math.pi*z)*(5*z+2))/4

def c2p(z):  # Returns the number of iterations it takes to get to a power of 2.
    count = 0
    while True:
        if math.log(z, 2) == math.floor(math.log(z, 2)):
            break
        else:
            z = c(z)
            count += 1  
    return count

@functools.lru_cache(maxsize=None)
def colcol(x, it): # Returns an colour hexvalue for each pixel. (just for art)
    org = x
    for i in range(0, it):
        x = c(x)
    a = '#'+hex(int(abs(org-x)))[2:]
    while True:
        if len(a) != 7:
            a += '0'
        else:
            break
    return a

##def c2pcolplot(xstart, xend, ystart, yend): # Plots the number of iterations it takes to a power of 2 as a colour for each pixel.
##    modxstart = (xend-xstart)//2
##    modystart = (yend-ystart)//2
##    orgx = xstart-1
##    ystart -= 1
##    for y in range(0-modystart, modystart):
##        turtle.seth(0)
##        ystart += 1
##        xstart = orgx
##        for x in range(0-modxstart, modxstart):
##            xstart += 1
##            turtle.up()
##            turtle.goto(x-1, y)
##            turtle.down()
##            a = '#'+hex(int(abs(xstart*ystart-c2p(xstart*ystart)))[2:]
##            while True:
##                if len(a) != 7:
##                    a += '0'
##            else:
##                break
##            turtle.color(a)
##            turtle.forward(1)
##            turtle.up()


def colcolplot(xstart, xend, ystart, yend, it): # Plots the numerical difference between the starting point and output value after a certain number of iterations as a colour for each pixel.
    modxstart = (xend-xstart)//2
    modystart = (yend-ystart)//2
    orgx = xstart-1
    ystart -= 1
    for y in range(0-modystart, modystart):
        turtle.seth(0)
        ystart += 1
        xstart = orgx
        for x in range(0-modxstart, modxstart):
            xstart += 1
            turtle.up()
            turtle.goto(x-1, y)
            turtle.down()
            turtle.color(colcol(xstart*ystart, it))
            turtle.forward(1)
            turtle.up()

def colplot(xstart, xend, ystart, yend, it): # Plots each pixel if the product of its x,y values is smaller than that put through a given number of iterations.
        modxstart = (xend-xstart)//2
        modystart = (yend-ystart)//2
        orgx = xstart-1
        ystart -= 1
        for y in range(0-modystart, modystart):
                turtle.seth(0)
                ystart += 1
                xstart = orgx
                for x in range(0-modxstart, modxstart):
                        xstart += 1
                        turtle.up()
                        turtle.goto(x-1, y)
                        prod = xstart*ystart
                        for i in range(0, it):
                                prod = c(prod)
                        if prod > xstart*ystart:
                                turtle.down()
                                turtle.forward(1)
                                turtle.up()

def funkyplot(xstart, xend, ystart, yend):
        modxstart = (xend-xstart)//2
        modystart = (yend-ystart)//2
        orgx = xstart-1
        ystart -= 1
        for y in range(0-modystart, modystart):
                turtle.seth(0)
                ystart += 1
                xstart = orgx
                for x in range(0-modxstart, modxstart):
                        xstart += 1
                        turtle.up()
                        turtle.goto(x-1, y)
                        itx = xstart
                        for i in range(0, y):
                                itx = c(itx)
                        if itx > x:
                                turtle.down()
                                turtle.forward(1)
                                turtle.up()

##turtle.tracer(0,0)
##colcolplot(1,400,1,400,3)
##turtle.update()
