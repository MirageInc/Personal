l = [1,2]

def f():
    a = 1
    for i in range(1, len(l)+1):
        a += l[i-1]*(len(l)-i)
    l.append(a)
