def na_czynniki_p(num):
    i = 2
    t = []
    while num != 1:
        if num % i == 0:
            t.append(i)
            while num%i == 0:
                num//=i
        i+=1
    return t
def reku(tab,idx,num):
    if len(tab) == idx:
        if num != 1:
            return num
        return 0
    suma = 0
    suma += reku(tab,idx+1,num)
    num*= tab[idx]
    suma+= reku(tab,idx+1,num)
    return suma

def func(num):
    return reku(na_czynniki_p(num),0,1)

print(func(60))
