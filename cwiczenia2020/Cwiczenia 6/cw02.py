def PrimeDivList(n): #zwraca listÄ™ podzielnikĂłw pierwszych w postaci tablicy
    l = []
    i = 2
    while n != 1:
        if n % i == 0:
            l.append(i)
        while n % i == 0:
            n //= i
        i+=1
    return l
def waga(tab,size):
    l_p = []
    for elem in range(size):
        for e in PrimeDivList(tab[elem]):
            for i in l_p:
                if e == i:
                    break
            else:
                l_p.append(e)
    return len(l_p)

def rekur(tab,index,tab1,tab2,tab3,idx1,idx2,idx3):
    if index >= len(tab):
        if waga(tab1,idx1) == waga(tab2,idx2) == waga(tab3,idx3):
            return True
        return False
    tab1[idx1] = tab[index]
    if rekur(tab,index+1,tab1,tab2,tab3,idx1+1,idx2,idx3):
        return True
    tab2[idx2] = tab[index]
    if rekur(tab,index+1,tab1,tab2,tab3,idx1,idx2+1,idx3):
        return True
    tab3[idx3] = tab[index]
    if rekur(tab,index+1,tab1,tab2,tab3,idx1,idx2,idx3+1):
        return True
    return False

def func(tab):
    tab1,tab2,tab3 = [0 for _ in range(len(tab))],[0 for _ in range(len(tab))],[0 for _ in range(len(tab))]
    return rekur(tab,0,tab1,tab2,tab3,0,0,0) 

print(func([2,3,6]))