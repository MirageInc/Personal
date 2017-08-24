import numpy as np
from PIL import Image
import random

def mandel(re, im, maxit, inf, order, mina=2, maxa=2, minb=2, maxb=2): # Adapted mandel() function which notes the points which the number touches as it escapes the orbit.
    z = complex(re, im)
    lz = []
    c,it = z,0

    for i in range(0, maxit):
        if z.real*z.real+z.imag*z.imag > inf*inf:
            break
        z,it = z**order+c,it+1

        if z.real > mina and z.real < maxa and z.imag > minb and z.imag < maxb:
            lz.append([z.real, z.imag]) # Here it adds a point to the list.

    if it+1 == maxit and z.real*z.real+z.imag*z.imag < inf: # if the point never escaped, then we do not return the list of its escape trajectory.
        return []
    else:
        return lz

def coord(floatx, floaty, xfm=[-2.0,2.0], yfm=[-2.0,2.0], xm=[0,99], ym=[0,99]): # This maps a point between the floating point range of the calculations to an integer xy coord.
    ratx = rerange(floatx, xfm, xm)
    raty = rerange(floaty, yfm, ym)
    return [ratx, raty]

def rerange(fx, xor=[1,2], xnr=[1,2]):
    ratx = int(abs(fx-xor[0]/(xor[1]-xor[0])*(xnr[1]-xnr[0])))
    return ratx

def buddhaplot(mina=-2.0, maxa=2.0, minb=-2.0, maxb=2.0, width=500, height=500, maxit=2000, inf=8, order=2, randit=40000):
    #l = np.zeros((width, height, 1))
    #l = [[[0,0,0] for i in range(height)] for j in range(width)]
    l = np.zeros((width,height,3),dtype=np.uint8)
    #turtle.colormode(255)
    maxp = 0

    for i in range(0, randit):
        c = mandel(random.uniform(mina, maxa), random.uniform(minb, maxb), maxit, inf, order, mina, maxa, minb, maxb)
        for j in range(0, len(c)):
            cxy = coord(c[j][0], c[j][1], [mina,maxa], [minb,maxb], [0, width], [0, height])
            #l[cxy[0],cxy[1]] += 1
            #l[cxy[0]][cxy[1]][0] += 1
            l[cxy[0],cxy[1],:] += 1
            l[cxy[0], cxy[1],:] %= 256

            print(l[cxy[0],cxy[1],0])
            if np.greater(l[cxy[0],cxy[1],0], maxp):
                maxp = l[cxy[0],cxy[1],:]

    for i in range(0, width):
        for j in range(0, height):
            l[i,j,:] = rerange(l[i,j,:], [0,maxp],[0,255])

    img = Image.fromarray(l)
    img.show()
    img.save('buddha.png')

        
    #turtle.up()
    #for x in range(-int(width/2), int(width/2)):
        #for y in range(-int(height/2), int(height/2)):
            #turtle.goto(x-1,y)
            #turtle.color((l[x,y], l[x,y], l[x,y]))
            #turtle.color((l[x][y]%256, l[x][y]%256, l[x][y]%256))
            #turtle.down()
            #turtle.forward(1)
            #turtle.up()

buddhaplot()

