#(x,y,z)
from math import sqrt
def check(tab,r):
    if len(tab) < 3:
        return False
    x = 0
    y = 0
    z = 0
    i = 0
    while i < len(tab):
        x += tab[i][0]
        y+= tab[i][1]
        z+= tab[i][2]
        i+=1
    dl = sqrt(((x/len(tab))**2)+((y/len(tab))**2)+((z/len(tab))**2))
    if dl <= r: 
        return True
    return False

def reku(tab,pomc,idx,r):
    if idx == len(tab):
        return check(pomc,r)
    if reku(tab,pomc,idx+1,r):
        return True
    pomc.append(tab[idx])
    if reku(tab,pomc,idx+1,r):
        return True
    pomc.pop()
    return False

def func(t,r):
    return reku(t,[],0,r)


print(check([(1,1,1),(1,1,1),(1,1,1)],100)) # to jest sam check nie nie glowan funckaj


