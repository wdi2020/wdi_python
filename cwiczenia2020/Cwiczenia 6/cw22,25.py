#zadanie 22 i 25 to to samo ...
def prime_div_list(num):
    tab = []
    i = 2
    while num != 1 and num != i:
        if num%i == 0:
            tab.append(i)
            while num%i ==0:
                num//=i
        i+=1
    return tab
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

def rekur(t,curr_idx,ilosc_skokow):
    if curr_idx >= len(t):
        return False
    if curr_idx  == len(t)-1:
        return ilosc_skokow
    if not czy_pierwsza(t[curr_idx]):
        for e in prime_div_list(t[curr_idx]):
            ret = rekur(t,curr_idx+e,ilosc_skokow+1)
            if ret != False:
                return ret
    return False

def func(t):
    ret = rekur(t,0,0)
    if ret == False:
        return -1
    return ret


print(func([6 for _ in range(101)]))