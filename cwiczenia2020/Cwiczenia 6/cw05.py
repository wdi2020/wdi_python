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

def check(pomocnicza,tab,idx_pom):
    pomocnicza[idx_pom] = len(tab)
    idx_pom += 1
    last = 0
    for j in range(idx_pom):
        i = pomocnicza[j]
        if not czy_pierwsza(na_binarnny(tab[last:i])):
            break
        last = i
    else:
        return True
    return False

def rekur(tab,idx_dziel,index,pomocnicza,idx_pom):
    for i in range(index+1,len(tab)):
        pomocnicza[idx_pom] = i
        idx_pom+=1
        print(pomocnicza,idx_pom)
        if check(pomocnicza,tab,idx_pom):
            return True
        if rekur(tab,idx_dziel,i,pomocnicza,idx_pom):
            return True
        idx_pom-=1
    return False

def func(tab):
    n = len(tab)
    pomocnicza = [0 for _ in range(n)]
    return rekur(tab,0,0,pomocnicza,0)

tab = [1,1,1,0,1,1]
print(func(tab))