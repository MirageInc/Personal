import math
pl = [2,3,5,7,11,13,17,19,23,29,31,37,41,43]
hc = [[1, 1], [2, 2], [4, 3], [6, 4], [12, 6], [24, 8], [36, 9], [48, 10], [60, 12], [120, 16], [180, 18], [240, 20], [360, 24], [720, 30], [840, 32], [1260, 36], [1680, 40], [2520, 48], [5040, 60], [7560, 64], [10080, 72], [15120, 80], [20160, 84], [25200, 90], [30240, 96], [45360, 100], [55440, 120]]
rlf = [1]

def isprime(n):
    c = True
    for i in range(2, math.ceil(n**0.5)+1):
        if n%i == 0:
            c = False
            break
    return c

def prime(n):
    if len(pl)-1 >= n:
        return pl[n-1]
    else:
        found = False
        a = pl[len(pl)-1]
        while found == False:
            a += 1.0
            if isprime(a) == True:
                pl.append(a)
            elif len(pl)-1 == n:
                found = True
                return pl[n-1]
                break

def relist(l):
    nl = [] # New list of [[thing, # of thing],...
    fl = [] # List of things already found.
    np = 0 # Cursor for how far previously looked
    finished = False
    while finished == False:
        for i in range(np, len(l)):
            if l[np] not in fl:
                break
            if np == len(l)-1:
                finished = True
                break
            else:
                np += 1
        nl.append([l[np], 0])
        fl.append(l[np])
        for i in range(1, len(l)):
            if l[i] == l[np]:
                nl[len(nl)-1][1] += 1
    del nl[len(nl)-1]
    nl[0][1] += 1
    return nl

def deprime(n):
    l = []
    primed = False # A value for whether the number has been fully decomposed.
    while primed == False:
        for i in range(1, int(n+1)):
            p = prime(i)
            if p > n:
                break
            if n%p == 0:
                l.append(p)
                n = n/p
        if n == 1:
            break
    return relist(l)

def mangoldt(n):
    if n > 1:
        l = deprime(n)
        if len(l) == 1:
            return math.log(l[0][0])
        else:
            return 0
    else:
        return 0

def chebyshev(n):
    a = 0
    for i in range(1, n+1):
        a += mangoldt(i)
    return a

def t(n):
    f = 2
    for i in range(2, n):
        if float(n/i) == int(n/i):
            f += 1
    return f

def bt(n):
    a = deprime(n)
    j = 1
    for i in range(0, len(a)):
        j *= (a[i][1]+1)
    return j

def factor(n):
    l = [1]
    for i in range(2, int(n//2+1)):
        if n%i == 0:
            l.append(i)
    l.append(n)
    return l

def h(n):
    if len(hc)-1 >= n:
        return hc[n]
    else:
        while True:
            m = int(hc[len(hc)-1][0]*1.16)
            while True:
                if bt(m) > hc[len(hc)-1][1]:
                    break
                else:
                    m += 1
            hc.append([m, bt(m)])
            if len(hc)-1 >= n:
                break
        return hc[n]

def rlfact(n):
    if len(rlf)-1 >= n:
        return rlf[n-1]
    else:
        found = False
        a = rlf[len(rlf)-1]
        while found == False:
            a += 1.0
            if len(factor(a)) > rlf[len(rlf)-1]:
                rlf.append(a)
            elif len(rlf)-1 == n:
                found = True
                return rlf[n-1]
                break

def s(n):
    a = deprime(n)
    j = 1
    for i in range(0, len(a)):
        j *= (((a[i][0]-(a[i][0]**(a[i][1]+1)))/(1-a[i][0]))+1)
    return j

def pi(x):
    x = int(math.ceil(x))
    count = 0
    for i in range(2, x):
        if isprime(i) == True:
            count += 1
    return count
