#III zadanie (4 punkty)
#- duże liczby naturalne reprezentowane są w postaci napisów. Prosze napisać procedurę mnożącą
#dwie duże liczby naturalne. Do procedury należy przekazać mnożone liczby oraz parametr, w którym
#zwrócony bedzie wynik mnożenia. Można założyć, że każdy z czynników posiada nie wiecej niż 100
#cyfr
def dodaj(a,b):
    reszta = 0
    i = 0
    ret = ""
    while len(a)!=0 or len(b)!=0:
        num=0
        if len(a)!=0:
            num += int(a[-1])
            a=a[0:-1]
        if len(b)!=0:
            num += int(b[-1])
            b=b[0:-1]
        num+=reszta
        if num >=10:
            reszta = num//10
        else:
            reszta=0
        ret = str(num%10) + ret
    if reszta!=0:
        ret = str(reszta)+ret
    return ret
def mnoz(a,b):
    cp = a
    t = []
    i = 0
    while b !="":
        mnoznik = int(b[-1])*(10**i)
        reszta = 0
        t.append([])
        for letter in cp[::-1]:
            num = (int(letter)*mnoznik)+reszta
            if num >=0:
                reszta = num//10
            else:
                reszta =0
            t[i].append(str(num%10))
        if reszta >0:
            for j in str(reszta)[::-1]:
                t[i].append(j)
        i+=1
        b = b[0:-1]
    suma = ""
    for i in range(0,len(t)):
        suma = dodaj(suma,(t[i][::-1]))
    return suma
print(mnoz("123456789","987654321"))