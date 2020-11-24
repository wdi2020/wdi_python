def ilosc_jedynek(num):
    count = 0
    while num != 0:
        if num %2 == 1:
            count+=1
        num//=2
    return count
def check(x1,x2,x3):
    sum1 = 0
    for i in x1:
        sum1+=ilosc_jedynek(i)
    sum2 = 0
    for i in x2:
        sum2+=ilosc_jedynek(i)
    sum3 = 0
    for i in x3:
        sum3+=ilosc_jedynek(i)
    return sum1 == sum2 == sum3
def r(tab,x1,x2,x3,idx):
    if len(tab) == idx:
        if x1 != [] and x2 != [] and x3 != []:
            if check(x1,x2,x3):
                return True
        return False
    x1.append(tab[idx])
    if r(tab,x1,x2,x3,idx+1):
        return True
    x1.pop()
    x2.append(tab[idx])
    if r(tab,x1,x2,x3,idx+1):
        return True
    x2.pop()
    x3.append(tab[idx])
    if r(tab,x1,x2,x3,idx+1):
        return True
    x3.pop()
    return False

def f(tab):
    return r(tab,[],[],[],0)


print(f([2,3,5,7,15]))
print(f([5,7,15]))