def ilosc_jedynek(num):
    count = 0
    while num != 0:
        if num %2 == 1:
            count+=1
        num//=2
    return count
def check(x1,x2,x3,idx1,idx2,idx3):
    sum1 = 0
    for j in range(idx1):
        i = x1[j]
        sum1+=ilosc_jedynek(i)
    sum2 = 0
    for j in range(idx2):
        i = x2[j]
        sum2+=ilosc_jedynek(i)
    sum3 = 0
    for j in range(idx3):
        i = x3[j]
        sum3+=ilosc_jedynek(i)
    return sum1 == sum2 == sum3
def r(tab,x1,x2,x3,idx,idx1,idx2,idx3):
    if len(tab) == idx:
        if idx1 != 0 and idx2 != 0 and idx3 != 0:
            if check(x1,x2,x3,idx1,idx2,idx3):
                return True
        return False
    x1[idx1] = tab[idx]
    if r(tab,x1,x2,x3,idx+1,idx1+1,idx2,idx3):
        return True
    x2[idx2] = tab[idx]
    if r(tab,x1,x2,x3,idx+1,idx1,idx2+1,idx3):
        return True
    x3[idx3] = tab[idx]
    if r(tab,x1,x2,x3,idx+1,idx1,idx2,idx3+1):
        return True
    return False

def f(tab):
    return r(tab,[0 for _ in range(len(tab))],[0 for _ in range(len(tab))],[0 for _ in range(len(tab))],0,0,0,0)


print(f([2,3,5,7,15])) #tru
print(f([5,7,15])) # false