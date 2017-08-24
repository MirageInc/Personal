import random
import math
import turtle
import winsound
import smtplib
import os
import time
import colorsys

global password
password = input('Enter password: ')
os.system('cls')
for i in range(0,100):
    print('\n')

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
            ntheta = ntheta+O-(k/(2*math.pi))*math.sin(2*math.pi*ntheta)
            ntheta %= 1
            if abs(ntheta-stheta) <= epsilon:
                time = i
                break
            elif i == maxit-1:
                time = maxit
                break
        l.append(time)
    return (sum(l)/len(l))

def colour(cyc):
    if cyc <= 10:
        return 'black'
    if cyc > 10 and cyc <= 50:
        return 'indigo'
    if cyc > 50 and cyc <= 100:
        return 'blue'
    if cyc > 100 and cyc <= 140:
        return 'green'
    if cyc > 140 and cyc <= 200:
        return 'yellow'
    if cyc > 200 and cyc <= 250:
        return 'orange'
    if cyc > 250:
        return 'red'

def rerange(n,olrange,nerange):
    if n > olrange[1] or n < olrange[0]:
        return 'ERROR: n not within OLD RANGE'
    else:
        olperc = (n-olrange[0])/(olrange[1]-olrange[0])
        return nerange[0]+olperc*(nerange[1]-nerange[0])



def circlemap(maxit, krange, Orange, samples, epsilon, width, height):

    for y in range(-int(height/2), int(height/2)):
        for x in range(-int(width/2), int(width/2)):
            currentk = rerange(y+(height/2),[0,height],krange)
            currentO = rerange(x+(width/2),[0,width],Orange)

            cycle = circle(maxit, currentk, currentO, samples, epsilon)
            turtle.up()
            turtle.goto(x-1,y)
            turtle.down()
            if cycle == 250:
                turtle.color('black')
            else:
                turtle.color(colorsys.hsv_to_rgb((cycle/250)**0.5,(cycle/250)**0.08,1))
            turtle.forward(1)

turtle.tracer(0,0)
circlemap(250, [0, 2*math.pi], [0, 1], 500, 0.001, 500, 500)
turtle.ht()
turtle.update()
winsound.Beep(10000,1000)
email()
