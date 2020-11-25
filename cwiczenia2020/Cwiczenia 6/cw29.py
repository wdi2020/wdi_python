#(x,y,z)
from math import sqrt
def check(tab,r,idx_pom):
    if idx_pom < 3:
        return False
    x = 0
    y = 0
    z = 0
    for i in range(idx_pom):
        x += tab[i][0]
        y+= tab[i][1]
        z+= tab[i][2]
    dl = sqrt(((x/len(tab))**2)+((y/len(tab))**2)+((z/len(tab))**2))
    if dl <= r: 
        return True
    return False

def reku(tab,pomc,idx,r,idx_pom):
    if idx == len(tab):
        return check(pomc,r,idx_pom)
    if reku(tab,pomc,idx+1,r,idx_pom):
        return True
    pomc[idx_pom] = tab[idx]
    if reku(tab,pomc,idx+1,r,idx_pom+1):
        return True
    return False

def func(t,r):
    return reku(t,[0 for _ in range(len(t))],0,r,0)


print(check([(1,1,1),(1,1,1),(1,1,1)],100,3)) # to jest sam check nie nie glowan funckaj


