import turtle
import math
import numpy as np
from PIL import Image
import colorsys
import time

def coz(z):
    return 0.5*(math.e**(complex(0, 1)*z)+math.e**-(complex(0, 1)*z))

def c(z):
    return 0.25*(2+7*z-coz(math.pi*z)*(2+5*z))

def colc(it,z,inf): # This is a function for use in the smoothcolouring algorithm - NOT BEING USED RIGHT NOW.
    return (it+1-math.log(math.log(abs(z))/math.log(2))/math.log(2))

def collatz(re, im, maxit, inf):
    a,it = complex(re, im),0
    for i in range(0, maxit):
        a = c(a)
        s = a.real*a.real+a.imag*a.imag
        if s < inf*inf:
            it += 1
        elif s > inf:
            break
    return [it, a]

def colplot(mina=-1.25, maxa=-1.15, minb=-0.05, maxb=0.05, xwidth=800.0, ywidth=800.0, maxit=1000, inf=10):

    b = minb
    turtle.up()

    for y in range(-int(ywidth/2), int(ywidth/2)):
        a = mina
        for x in range(-int(xwidth/2), int(xwidth/2)):
            turtle.goto(x-1, y)

            ab = collatz(a,b, maxit, inf)
            
            orga,orgb,count = a,b,0
            
 #           while count <= maxit:
 #               asq,bsq,tab = a**2.0,b**2.0,2.0*a*b
 #               
 #               a,b = asq-bsq+orga,tab+orgb
                
 #               if asq**2 + bsq**2 > inf:
 #                   break

 #               count += 1.0

            if ab[0] == maxit:
                turtle.color("black")
                turtle.down()
                turtle.forward(1)
                turtle.up()
            
            if ab[0] < maxit:
                nsmooth = abs(ab[0]+1-math.log(math.log((ab[1].real**2+ab[1].imag**2)**0.5, 10), 2)/math.log(2))
                turtle.color(colorsys.hsv_to_rgb((10*nsmooth)**0.04, 1, 1))
                turtle.down()
                turtle.forward(1)
                turtle.up()

#                cl = (math.log(math.log(inf, 10), 10)/math.log(2, 10)-math.log(math.log(count, 10), 10)/math.log(2, 10)+count)/maxit
#                turtle.color(colorsys.hsv_to_rgb(cl, 1, 1))

            a,b = orga+abs(mina-maxa)/xwidth,orgb
        b = orgb+abs(minb-maxb)/ywidth
        turtle.ht()

def colimage(mina=-2.0, maxa=2.0, minb=-2.0, maxb=2.0, width=300, height=300, maxit=500, inf=10):

    l = np.zeros((width,height,3),dtype=np.uint8) # Creates a numpy array with the right dimensions.
    l.fill(255)
    b = minb

    for y in range(0, height):
        a = mina
        for x in range(0, width):
            
            ab = collatz(a, b, maxit, inf)

            #if ab[0] == maxit: # This is supposed just colour the right stuff black rather than use colours for debugging purposes.
                #l[y,x,:] = 255

            if ab[0]+1 == maxit:
                print(1)
                l[y,x,:] = 0

            if ab[0] < maxit:
                smoothit = colc(ab[0], ab[1], inf)
                l[y, x] = colorsys.hsv_to_rgb(10*smoothit, 1, 1)
                
            a += abs(mina-maxa)/width
        b += abs(minb-maxb)/height

    img = Image.fromarray(l, "RGB") # Fairly self-explanatory.

    img.show()
    img.save("colf.png")

turtle.tracer(0,0)
colplot()
turtle.update()
