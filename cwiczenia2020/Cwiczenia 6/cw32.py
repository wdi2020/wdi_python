def check(t1,t2,idx1,idx2):
    suma1 = 0
    for i in range(idx1):
        suma1 += t1[i]
    suma2 = 0
    for i in range(idx2):
        suma2 += t2[i]
    return suma1 == suma2

def reku(tab,t1,t2,idx,k,idx1,idx2):
    if idx1 + idx2 == k:
        if check(t1,t2,idx1,idx2):
            return True
        return False
    if idx == len(tab):
        return False
    
    if reku(tab,t1,t2,idx+1,k,idx1,idx2):
        return True
    
    t1[idx1] = tab[idx]
    if reku(tab,t1,t2,idx+1,k,idx1+1,idx2):
        return True
    
    t2[idx2] = tab[idx]
    if reku(tab,t1,t2,idx+1,k,idx1,idx2+1):
        return True

    return False

def func(tab,k):
    return reku(tab,[0 for _ in range(len(tab))],[0 for _ in range(len(tab))],0,k,0,0)


print(func([12,24,36,1],4)) #false