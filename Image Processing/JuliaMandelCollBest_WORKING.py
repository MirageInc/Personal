from math import *
import cmath
import numpy as np
from PIL import Image
import colorsys
import winsound
import random
import smtplib
import os
import time
from numba import jit

#import matplotlib as m

# Remember -1.25 to 1.25

#global password
#password = input('Enter password: ')
#os.system('cls')
#for i in range(0,100):
#    print('\n')

def email():
    addr = 'iskym9@gmail.com'
    msg = "\r\n".join([
    "From: iskym9@gmail.com",
    "To: iskym9@gmail.com",
    "Subject: COMPUTED!",
    '',
    '['+time.strftime('%H')+':'+time.strftime('%M')+':'+time.strftime('%S')+']'
    ])
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(addr,password)
    server.sendmail(addr, addr, msg)
    server.quit()

def circle(maxit, k, O, samplen, epsilon):
    l = []
    for j in range(0, samplen):
        stheta = random.uniform(0,1)
        ntheta = stheta
        for i in range(0, maxit):
            ntheta = ntheta+O-(k/(2*pi))*sin(2*pi*ntheta)
            ntheta %= 1
            if abs(ntheta-stheta) <= epsilon:
                time = i
                break
            elif i == maxit-1:
                time = maxit
                break
        l.append(time)
    return (sum(l)/len(l))

def mandel(re, im, maxit, inf, order):
    z = complex(re, im)
    c,it = z,0

    for i in range(0, maxit):
        if z.real*z.real+z.imag*z.imag > inf*inf:
            break
        z,it = (z**order)+c,it+1
    return it,z

def mandelc(it,z):
    return (it+1-log(log(abs(z)))/log(2))

@jit
def julia(re, im, c, maxit, inf, order):
    z,it = complex(re, im),0

    for i in range(0, maxit):
        if z.real*z.real+z.imag*z.imag > inf*inf:
            break
        z,it = (z**order)+c,it+1
    return it,z

def clifford(re, im, maxit, inf, order):
    z = complex(re, im)
    c,dist = z,10**6

    for i in range(0, maxit):
        d = abs(z)
        if d > inf*inf:
            break
        if d < dist:
            dist = d
        z = (z**order)+c
    return dist,z

@jit
def c(z):
    return 0.25*(2+7*z-cmath.cos(pi*z)*(2+5*z))

@jit
def collatz(re, im, maxit, inf):
    z,it = complex(re, im),0

    for i in range(0, maxit):
        if z.real*z.real+z.imag*z.imag > inf*inf:
            break
        z,it = c(z),it+1
    return it,z

def imagebrot(mina=-2.0, maxa=0.5, minb=-1.25, maxb=1.25, width=24000, height=24000, maxit=1000, inf=500, order=2):
    sect = (maxb-minb)/float(height/1000)
    
    for i in range(0, int(height/1000)):
        
        l = np.zeros((width, 1000, 3), dtype=np.uint8)
        nminb = minb+(sect*i)
        nmaxb = nminb+sect
        b = nminb

        for y in range(0, 1000):
            a = mina
            for x in range(0, width):
            
                ab = mandel(a, b, maxit, inf, order)

#               if ab[0] == maxit:
#                   l[x,y,:] = 255

                if ab[0] < maxit:
                    #smoothit = mandelc(ab[0], ab[1])
                    nsmooth = abs(ab[0]+1-log(log((ab[1].real**2+ab[1].imag**2)**0.5, 10), 2)/log(2))
                    l[x, y,:] = colorsys.hsv_to_rgb(nsmooth**0.05,50,1)
                
                a += abs(mina-maxa)/width
            b += abs(minb-maxb)/height

        img = Image.fromarray(l, "RGB")
        img.save("mandel"+str(i)+".png")
        winsound.Beep(10000,1000)

def cliffordbrot(mina=-2.0, maxa=0.5, minb=-1.25, maxb=1.25, width=50000, height=50000, maxit=100, inf=100, order=2):
    l = np.zeros((width,height,3),dtype=np.uint8)
    b = minb

    for y in range(0, height):
        a = mina
        for x in range(0, width):
            
            ab = clifford(a, b, maxit, inf, order)

#            if ab[0] == maxit:
#                l[x,y,:] = 255

            if ab[0] < maxit:
                #smoothit = mandelc(ab[0], ab[1])
                #nsmooth = abs(ab[0]+1-log(log((ab[1].real**2+ab[1].imag**2)**0.5, 10), 2)/log(2))
                l[x, y,:] = colorsys.hsv_to_rgb((ab[0]*10)**0.2,10,20)
                
            a += abs(mina-maxa)/width
        b += abs(minb-maxb)/height

    img = Image.fromarray(l, "RGB")
    img.save("clifford.png")

@jit
def julimage(mina=-1.6, maxa=1.6, minb=0, maxb=1.2, width=28000, height=10000, maxit=750, inf=100, order=2, c=complex(-0.835,0.232)):
    sect = (maxb-minb)/float(height/1000)
    
    for i in range(0, int(height/1000)):
        
        l = np.zeros((width, 1000, 3), dtype=np.uint8)
        nminb = minb+(sect*i)
        nmaxb = nminb+sect
        b = nminb
        
        for y in range(0, 1000):
            a = mina
            for x in range(0, width):
            
                ab = julia(a, b, c, maxit, inf, order)

#               if ab[0] == maxit:
#                   l[x,y,:] = 255

                if a == 0 and b == 0:
                    l[x, y,0],l[x,y,1],l[x,y,2] = 0,0,0

                if ab[0] < maxit:
                    #smoothit = mandelc(ab[0], ab[1])
                    nsmooth = (log(log(inf, 10), 10)/log(2, 10)-log(log(ab[0], 10), 10)/log(2, 10)+ab[0])/maxit
                    l[x, y,:] = colorsys.hsv_to_rgb((5*nsmooth)**0.5,100,15)
                
                a += abs(mina-maxa)/width
            b += abs(minb-maxb)/height

        img = Image.fromarray(l, "RGB")
        img.save("julia"+str(i)+".png")

@jit
def colimage(mina=-1.25, maxa=0.25, minb=-0.75, maxb=0.75, width=50000, height=50000, maxit=1000, inf=100):
    sect = (maxb-minb)/float(height/1000)
    
    for i in range(0, int(height/1000)):
    
        l = np.zeros((width, 1000, 3), dtype=np.uint8)
        nminb = minb+(sect*i)
        nmaxb = nminb+sect
        b = nminb

        for y in range(0, 1000):
            a = mina
            for x in range(0, width):
            
                ab = collatz(a, b, maxit, inf)

#               if ab[0] == maxit:
#                   l[x,y,:] = 255

                if ab[0] < maxit:
                    #smoothit = mandelc(ab[0], ab[1])
                    nsmooth = abs(ab[0]+1-log(log((ab[1].real**2+ab[1].imag**2)**0.5, 10), 2)/log(2))
                    l[x, y,:] = colorsys.hsv_to_rgb((10*nsmooth)**0.05,100,1)
                
                a += abs(mina-maxa)/width
            b += abs(minb-maxb)/height

        img = Image.fromarray(l, "RGB")
        img.save("collatz"+str(i)+".png")
        winsound.Beep(10000,1000)
        

def circlimage(mina=0, maxa=2*pi, minb=0, maxb=1, width=50000, height=50000, maxit=500, samples=100, epsilon=0.001):
    l = np.zeros((width,height,3),dtype=np.uint8)
    b = minb

    for y in range(0, height):
        a = mina
        for x in range(0, width):
            
            ab = circle(maxit, a, b, samples, epsilon)


            if ab >= 10:
                #smoothit = mandelc(ab[0], ab[1])
                #nsmooth = abs(ab[0]+1-log(log((ab[1].real**2+ab[1].imag**2)**0.5, 10), 2)/log(2))
                l[x, y,:] = colorsys.hsv_to_rgb((ab/500),100,1)
                
            a += abs(mina-maxa)/width
        b += abs(minb-maxb)/height

    img = Image.fromarray(l, "RGB")
    img.save("circle.png")

colimage()
