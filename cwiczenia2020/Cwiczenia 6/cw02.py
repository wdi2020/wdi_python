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

def waga(tab):
    l_p = []
    for elem in tab:
        for e in PrimeDivList(elem):
            for i in l_p:
                if e == i:
                    break
            else:
                l_p.append(e)
    return len(l_p)

def rekur(tab,index,tryb,tab1,tab2,tab3):
    if index >= len(tab):
        if waga(tab1) == waga(tab2) and waga(tab1) == waga(tab3):
            return True
        return False
    if tryb == 0:
        li = list(tab1)
        li.append(tab[index])
        tab1 = tuple(li)
    elif tryb == 1:
        li = list(tab3)
        li.append(tab[index])
        tab2 = tuple(li)
    elif tryb == 2:
        li = list(tab3)
        li.append(tab[index])
        tab3 = tuple(li)
    #end if
    return rekur(tab,index+1,0,tab1,tab2,tab3) or rekur(tab,index+1,1,tab1,tab2,tab3) or rekur(tab,index+1,2,tab1,tab2,tab3)

def func(tab):
    tab1,tab2,tab3 = tuple(),tuple(),tuple()
    return rekur(tab,0,0,tab1,tab2,tab3) or rekur(tab,0,1,tab1,tab2,tab3) or rekur(tab,0,2,tab1,tab2,tab3)


print(func([2,3,5]))