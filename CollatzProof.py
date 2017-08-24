import math

def sim(m, n):
	a = ((m+n)/2)/max(m, n)
	return a**1.5

def perm(n):
    l = []
    for i in range(1, 2**n-1):
        st = bin(i)[2:]
        if len(st) != n:
            empty = ''
            for j in range(0, n-len(st)):
                empty += '0'
            empty += st
            st = empty
        l.append(st)
    return l

def solve(l):
    if l[0] == 0:
        return l[1]
    if l[0] == 1:
        return "Undefined"
    else:
        return -(l[1]/(l[0]-1))


def cyclist(n):
    l = perm(n)
    outputl = []
    for i in range(0, len(l)):
        num = [1,0]
        for k in range(0, len(l[i])):
            if l[i][k] == '1':
                num[0] *= 3
                num[1] *= 3
                num[1] += 1
            if l[i][k] == '0':
                num[0] /= 2
                num[1] /= 2
        outputl.append([l[i], solve(num)])
    return outputl

def cycheck(n):
    l = perm(n)
    outputl = []
    for i in range(0, len(l)):
        if bincheck(l[i]) == True:
            num = [1,0]
            for k in range(0, len(l[i])):
                if l[i][k] == '1':
                    num[0] *= 3
                    num[1] *= 3
                    num[1] += 1
                if l[i][k] == '0':
                    num[0] /= 2
                    num[1] /= 2
                x = solve(num)
            if check([l[i], x]) == True:
                print(l[i], solve(num))

def bincheck(st):
    zeroc = 0.0
    for i in range(0, len(st)-1):
        if st[i] == '1' and st[i+1] == '1':
            return False
        if st[i] == '0':
            zeroc += 1
    if sim(zeroc/len(st), 3/5.0) < 0.82:
        return False
    else:
        return True

def check(l): # Checks if a given potential cycle is legitimate.
    if math.ceil(l[1]) != float(l[1]) or l[1] < 0 or int(l[1])%2 == 0 or l[1] == 1 or l[1] == 2 or l[1] == 4 or (int(l[1])%2 != 0 and l[0][0] == '0'):
        return False
    else:
        cursor = 0
        n = l[1]
        while True:
            for i in range(0, len(l[0])-cursor):
                if l[0][cursor] == '1':
                    break
                else:
                    cursor += 1
            pof2 = 0
            for i in range(1, len(l[0])-cursor):
                if l[0][cursor+i] == '1':
                    break
                else:
                    pof2 += 1
            if (n*3+1)%(2**pof2) != 0:
                return False
            if cursor+1 == len(l[0])-1:
                return True
            else:
                cursor += 1
                n = (n*3+1)/(2**pof2)
