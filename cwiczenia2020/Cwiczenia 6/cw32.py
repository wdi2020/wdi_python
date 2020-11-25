def check(t1,t2):
    suma1 = 0
    for i in t1:
        suma1 += i
    suma2 = 0
    for i in t2:
        suma2 += i
    return suma1 == suma2

def reku(tab,t1,t2,idx,k):
    if len(t1) + len(t2) == k:
        if check(t1,t2):
            return True
        return False
    if idx == len(tab):
        return False
    
    if reku(tab,t1,t2,idx+1,k):
        return True
    
    t1.append(tab[idx])
    if reku(tab,t1,t2,idx+1,k):
        return True
    t1.pop()
    
    t2.append(tab[idx])
    if reku(tab,t1,t2,idx+1,k):
        return True
    t2.pop()

    return False

def func(tab,k):
    return reku(tab,[],[],0,k)


print(func([12,24,36,1],4)) #false