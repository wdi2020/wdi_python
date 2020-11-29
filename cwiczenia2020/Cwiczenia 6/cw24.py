#(x1,y1)
def check(tab,t1,t2,min_suma,idx1,idx2):
    if idx1 == 0 or idx2 == 0:
        return min_suma
    x1 = 0
    y1 = 0
    for i in range(idx1):
        x1 += tab[t1[i]][0]
        y1 += tab[t1[i]][1]
    x1 /= idx1
    y1/= idx1
    x2 = 0
    y2 = 0
    for i in range(idx2):
        x2 += tab[t2[i]][0]
        y2 += tab[t2[i]][1]
    x2 /= idx2
    y2 /= idx2
    dl = ((x1-x2)**2 + (y1-y2)**2)**.5
    if min_suma != -1:
        min_suma = min(dl,min_suma)
    else:
        min_suma = dl
    return min_suma

def reku(tab,index,t1,t2,min_suma,idx1,idx2):
    if index == len(tab):
        return check(tab,t1,t2,min_suma,idx1,idx2)
    suma = reku(tab,index+1,t1,t2,min_suma,idx1,idx2)
    if min_suma == -1:
        min_suma = suma
    else:
        min_suma = min(min_suma,suma)

    t1[idx1] = index
    suma = reku(tab,index+1,t1,t2,min_suma,idx1+1,idx2)
    if min_suma == -1:
        min_suma = suma
    else:
        min_suma = min(min_suma,suma)

    t2[idx2] = index
    suma = reku(tab,index+1,t1,t2,min_suma,idx1,idx2+1)
    if min_suma == -1:
        min_suma = suma
    else:
        min_suma = min(min_suma,suma)

    return min_suma
def func(tab):
    return reku(tab,0,[0 for _ in range(len(tab))],[0 for _ in range(len(tab))],-1,0,0)

tab = [(0,0),(1,2),(2,1),(100000000,1000000000)]
print(func(tab))
