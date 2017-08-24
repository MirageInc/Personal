
def sylvester(start=3.0/4, end=2.0, steps=6):
    l = []
    for i in range(0, steps):
        c = 2
        while True:
            check = 1.0/c
            if start+check < end:
                l.append(c)
                start += check
                break
            else:
                c += 1
    return [l, start]

print(sylvester())
