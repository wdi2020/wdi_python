def czynniki_pierwsze(num):
    t = []
    i = 2
    while num != 1:
        if num%i==0:
            t.append(i)
            while num%i==0:
                num//=i
        i+=1
    return t

def przesun(tab,idx):
    if idx >= len(tab):
        return False
    if idx == len(tab)-1:
        return True
    for num in czynniki_pierwsze(tab[idx]):
        if przesun(tab,idx+num):
            return True
    return False

from random import randint
tab = [randint(2,100) for _ in range(100)]
print(przesun(tab,0))
