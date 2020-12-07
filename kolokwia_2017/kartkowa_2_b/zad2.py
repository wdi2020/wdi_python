#Dana jest tablica t[N] zawieraj¡ca liczby naturalne. Prosz¦ napisa¢ funkcj¦, która odpowiada na pytanie,
#czy z elementów tablicy (niekoniecznie wszystkich) mo»na utworzy¢ dwa równoliczne, niepuste podzbiory
#o jednakowej sumie elementów. Do funkcji nale»y przekaza¢ wyª¡cznie tablic¦ t, funkcja powinna zwróci¢
#warto±¢ typu bool.
def suma(t,idx):
    o = 0
    for i in range(idx):
        o += t[i]
    return o
def reku(tab,index,t1,idx1,t2,idx2):
    if index == len(tab):
        if idx1 == idx2 and suma(t1,idx1) == suma(t2,idx2):
            return True
        return False
    if reku(tab,index+1,t1,idx1,t2,idx2):
        return True
    t1[idx1] = tab[index]
    if reku(tab,index+1,t1,idx+1,t2,idx2):
        return True
    t2[idx2] = tab[index]
    if reku(tab,index+1,t1,idx1,t2,idx2+1):
        return True
    return False
def strt(tab):
    t1 = [0 for _ in range(len(tab))]
    t2 = [0 for _ in range(len(tab))]
    return reku(tab,0,t1,0,t2,0)
