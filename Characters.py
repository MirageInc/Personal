import math
import itertools

pl = [2,3,5,7,11,13,17,19,23,29,31,37,41,43]

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

p = map(prime, itertools.count())
next(p)
pl = [int(next(p)) for i in range(0, 100)]

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

def residue(n):
    l = [i for i in range(2, n)]
    pn = deprime(n)
    for fact in pn:
        nl=[]
        for item in l:
            fact_i = deprime(item)
            found = False
            for facti in fact_i:
                if facti[0] == fact[0]:
                    found = True
            if found == False:
                nl.append(item)
        l = nl
    return ([1]+l, n)

def orbit(res):
    l = []
    for i in res[0]:
        orb = i
        count = 1
        while True:
            count += 1
            orb *= i
            orb %= res[1]
            if orb == 1:
                break
        l.append(count)
    return tuple(l)

def gens(res, find):
    genl = []
    orb = orbit(res)
    for i in orb:
        if i == len(res[0]):
            genl.append(i)
    
    for k in range(2,len(res[0])):
        comb = list(itertools.combinations(res[0], k))
        for g in comb:
            if g[0] == 1:
                continue
            else:
                gpowl = [[j for j in range(1,orb[res[0].index(g[n])])] for n in range(0,len(g))]
                power_list = itertools.product(*gpowl)
                generated = []
                for pow in power_list:
                    powered = [(g[i]**pow[i])%res[1] for i in range(0, len(g))]
                    n = 1
                    for i in powered:
                        n *= i
                    n %= res[1]
                    if n not in generated:
                        generated.append(n)
                        
                if set(generated) == set(res[0]):
                    new = True
                    for item in genl:
                        if set(item) == set(generated):
                            new = False
                            break
                    if new == True:
                        genl.append(g)
    return genl