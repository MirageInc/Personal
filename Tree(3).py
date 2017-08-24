import turtle
import math

def tree(br=2, initl=110, lmod=0.5, layers=5, isd=True, dsize=4, dmod=0.85, startx=0, starty=-100, swidth=10):
    tangle = 180/(br+1) # The turning angle.
    global l
    l = []
    c = 0 # Changes the colour over time.

    if isd != True:
        dsize = 0

    turtle.speed(0)
    turtle.width(swidth)
    turtle.up() # Initial branch drawing.
    turtle.goto(startx, starty)
    turtle.seth(90)
    turtle.dot(dsize)
    turtle.down()
    turtle.forward(initl)
    l.append([[0, turtle.pos()]]) # The array is like this: [[ angle_offset, (x, y) ]... and there are many of these for each point in a sub-array for each layer.
    
    for i in range(0, layers):
        c += 10
        initl *= lmod # Reduces the length of each branch with the modifier.
        swidth *= lmod
        dsize *= dmod
        turtle.width(swidth)
        l.append([])
        
        for j in range(0, len(l[i])):
            turtle.up()
            turtle.goto(l[i][j][1][0],l[i][j][1][1]) # This goes to each point in the array and branches.
            turtle.dot(dsize)
            turtle.seth(l[i][j][0])

            nl = []

            for k in range(1, br+1):
                turtle.left(tangle)
                turtle.down()
                turtle.forward(initl)
                nl.append([turtle.heading()-90, turtle.pos()]) # This stores each branching point in a new sub-array. 
                turtle.up()
                turtle.goto(l[i][j][1][0],l[i][j][1][1])

            l[i+1] += nl # The new sub-array is added to super-array.

def hildraw(s, leng):
    for i in range(0, len(s[0])):
        if s[0][i] == 'F':
            turtle.forward(leng)
        if s[0][i] == '-':
            turtle.left(90)
        if s[0][i] == '+':
            turtle.right(90)

def lndtree(it):
    s = "X"
    for i in range(0, it):
        ns = ''
        for j in range(0, len(s)):
            if s[j] == '-' or s[j] == '+' or s[j] == ']' or s[j] == '[':
                ns += s[j]
            if s[j] == 'X':
                ns += "F-[[X]+X]+F[+FX]-X"
            if s[j] == 'F':
                ns += "FF"
        s = ns
    return s

def lndtreedraw(s, leng):
    l = []
    for i in range(0, len(s)):
        if s[i] == 'F':
            turtle.forward(leng)
        if s[i] == '-':
            turtle.left(25)
        if s[i] == '+':
            turtle.right(25)
        if s[i] == '[':
            l.append([turtle.pos(), turtle.heading()])
        if s[i] == ']':
            turtle.up()
            turtle.goto(l[len(l)-1][0])
            turtle.seth(l[len(l)-1][1])
            turtle.down()
            del l[len(l)-1]

def lndhill(it):
    s = "A"
    for i in range(0, it):
        ns = ''
        for j in range(0, len(s)):
            if s[j] == '-' or s[j] == '+' or s[j] == 'F':
                ns += s[j]
            if s[j] == 'A':
                ns += "-BF+AFA+FB-"
            if s[j] == 'B':
                ns += "+AF-BFB-FA+"
        s = ns
    return s

def lnd3hill(it):
    s = "A"
    for i in range(0, it):
        ns = ''
        for j in range(0, len(s)):
            if s[j] == '-' or s[j] == '+' or s[j] == 'F' or s[j] == '&' or s[j] == '^' or s[j] == '/' or s[j] == '|':
                ns += s[j]
            if s[j] == 'A':
                ns += "B-F+CFC+F-D&F^D-F+&&CDC+F+B//"
            if s[j] == 'B':
                ns += "A&F^CFB^F^D^^-F-D^|F^B|FC^F^A//"
            if s[j] == 'C':
                ns += "|D^|F^B-F+C^F^A&&FA&F^C+F+B^F^D//"
            if s[j] == 'B':
                ns += "|CFB-F+B|FA&F^A&&FB-F+B|FC//"
        s = ns
    return s

def lred(l): # Formats a graph-array for drawing using left->right algorithm.
    nl = []
    mx = 1
    for i in l:
        nl.append(sorted(i)) # Sorts it so that each pair has the lowest of the 2 come first to make it easier to iterate through.
        if max(i) > max:
            mx = max(i)
    nl = sorted(nl)
    for j in range(0, len(nl)-2):
        for i in range(1, len(nl)):
            found = False
            for k in range(0, i):
                if nl[k][0] == nl[i][0] or nl[k][1] == nl[i][0]: # Sorts it so that if the first of a pair is not mentioned previously in the array, you flip the pair. and resort.
                    found = True
                    break

            if found == False:
                nl.append([nl[i][1], nl[i][0]])
                del nl[i]
                nl = sorted(nl)
    return nl

def maxarr(l):
    maxa = 1
    for i in l:
        if i[0] > maxa:
            maxa = i[0]
    return maxa

def checka(v, arr):
    b = False
    for i in range(0, len(arr)):
        if arr[i][0] == v:
            b = i
            break
    return b

def f(l): # The number of Caitlyn's ways of buying bicycles.
    nl = []
    for i in range(0, len(l)):
        if i == len(l)-1:
            nl.append(1)
        else:
            nl.append(l[i]+l[i+1])
    nnl = []
    for j in range(0, len(nl)):
        if j == 0:
            nnl.append(nl[0])
        else:
            nnl.append(nl[j]+nl[j-1])
    if len(nnl) < 5:
        nnl.append(1)
    l = nnl
    return nnl

def p(l):
    nl = []
    for i in range(0, len(l)):
        if i == len(l)-1:
            nl.append(1)
        else:
            nl.append(l[i]+l[i+1])
    nnl = []
    for i in range(0, len(nl)):
        if i == 0:
            nnl.append(nl[0])
        if i == len(nl)-1:
            nnl.append(1)
        else:
            nnl.append(nl[i]+nl[i+1])
    return nnl

def fib(l): # Interesting combinatoric way (by chance) to generate alternating Fibonacci numbers.
    a = 1
    n = len(l)+1
    for i in range(0, len(l)):
        a += (n-(i+1))*l[i]
        if i > 2:
            for m in range(2, i+1):
                a += comb(n-i, m)
    l.append(a)

def fact(n):
    a = 1
    for i in range(2, n+1):
        a*= i
    return a

def comb(n, k):
    return int((fact(n)/(fact(k)*fact(n-k))))

def g(l):
    a = 1
    n = len(l)+1
    for i in range(0, len(l)):
        a += (n-(i+1))*l[i]
        if (i+1) > 2:
            for m in range(2, i+2):
                a += comb(n-i, m)
                print(comb(n-i, m))
    l.append(a)

class Graph():
    def __init__(self, nV=1, E=[]):
        self.__nV = nV
        self.__E = E

    @property
    def nV(self):
        return self.__nV
    def order(self):
        return self.nV
    def size(self):
        return len(self.E)
    @property
    def E(self):
        return self.__E
    @nV.setter
    def nV(self, nV):
        self.__nV = nV
    @E.setter
    def E(self, E):
        self.__E = E

    def ready(self):
        self.E = lred(self.E)

    def treeDraw(self):
        self.ready()
        ppos = [[1, 0, 0]] # Array of currently drawn points along with x,y coords.
        ce = self.E
        for i in range(1, maxarr(self.E)+1): # Iterates through list the number of times that a drawing point occurs.
            turtle.up()
            turtle.goto(ppos[i-1][0],ppos[i-1][1])
            count = 0 # Num of points not-drawn connected to current point.
            it = 0 # Num of points connected to current point.
            
            for j in ce:
                if j[0] == i and checka(j[1], ppos) == False:
                    count += 1

            for j in ce:
                if j[0] == i:
                    it += 1

            angle = 180.0/(count+1)

            for k in range(0, it):
                a = checka(ce[k][1], ppos) # If the point has already been drawn, then goto its x,y coords.
                if a != False:
                    turtle.down()
                    turtle.goto(ppos[a][1], ppos[a][2])
                    turtle.up()
                    turtle.goto(ppos[i-1][0],ppos[i-1][1])
                else: # If it hasn't, branch off from the current point and add it to the array of drawn points.
                    turtle.left(angle)
                    turtle.forward(20)
                    ppos.append([ce[k][1], turtle.xcor(), turtle.ycor()])
            del ce[0:k]
                    
    def circDraw(self, r):
        intangle = 360.0/self.nV
        turtle.up()
        th = 360/(2*self.nV)
        side = abs(2.0*r*math.sin(th))
        turtle.goto(0-side/2, 0-r*1.3)
        turtle.seth(0)
        nodes = []
        turtle.color('blue')
        for i in range(0, self.nV):
            turtle.forward(side)
            turtle.left(intangle)
            turtle.dot(10)
            nodes.append(turtle.pos())

        turtle.width(2)
        turtle.color('black')
        for el in self.E:
            turtle.goto(nodes[el[0]-1])
            turtle.down()
            turtle.goto(nodes[el[1]-1])
            turtle.up()

l = [1,2,5]

