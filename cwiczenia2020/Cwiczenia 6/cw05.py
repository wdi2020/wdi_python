def czy_pierwsza(num):
    if num <=1:
        return False
    if num ==2 or num ==3:
        return True
    if num %2==0 or num%3==0:
        return False
    i = 6
    while (i-1)**2<=num:
        if num %(i-1) == 0:
            return False
        if num%(i+1) == 0:
            return False
        i+=6
    return True

def na_binarnny(tab):
    num = 0
    waga = len(tab)-1
    i = 0
    while i < len(tab):
        num += tab[i]*(2**(waga))
        i+=1
        waga-=1
    return num

def check(pomocnicza,tab):
    pomocnicza.append(len(tab))
    last = 0
    for i in pomocnicza:
        if not czy_pierwsza(na_binarnny(tab[last:i-1])):
            break
        last = i
    else:
        pomocnicza.pop()
        return True
    pomocnicza.pop()
    return False

def rekur(tab,idx_dziel,index,pomocnicza):
    for i in range(index+1,len(tab)):
        pomocnicza.append(i)
        if check(pomocnicza,tab):
            return True
        if rekur(tab,idx_dziel,i,pomocnicza):
            return True
        pomocnicza.pop()
    return False

def func(tab):
    n = len(tab)
    pomocnicza = list()
    return rekur(tab,0,0,pomocnicza)

tab = [1,1,1,0,1,1]
print(func(tab))