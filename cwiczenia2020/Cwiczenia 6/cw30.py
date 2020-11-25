from math import sqrt
def check(tab,r,k,idx):
    if idx%3 != 0 or idx == 0:
        return False
    if idx >= k:
        return False
    x = 0
    y = 0
    i = 0
    while i < idx:
        x += tab[i][0]
        y += tab[i][1]
        i+=1
    x /= i
    y /= i
    dl = sqrt((x**2) + (y**2))
    if dl <= r:
        return True
    return False

#(x,y)
def reku(tab,pomc,idx,r,k,pom_idx):
    if len(tab) == idx:
        return check(pomc,r,k,pom_idx)
    if reku(tab,pomc,idx+1,r,k,pom_idx):
        return True
    pomc[pom_idx] = tab[idx]
    if reku(tab,pomc,idx+1,r,k,pom_idx+1):
        return True
    return False


def func(tab,r,k):
    return reku(tab,[0 for _ in range(len(tab))],0,r,k,0)
