def check(tab,r,k):
    if len(tab)%3 == 0 and len(tab) != 0:
        return False
    if len(tab) >= k:
        return False
    x = 0
    y = 0
    i = 0
    while i < len(tab):
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
def reku(tab,pomc,idx,r,k):
    if len(tab) == idx:
        return check(pomc,r,k)
    if reku(tab,pomc,idx+1,r,k):
        return True
    pomc.append(tab[idx])
    if reku(tab,pomc,idx+1,r,k):
        return True
    pomc.pop()
    return False


def func(tab,r,k):
    return reku(tab,[],0,r,k)
