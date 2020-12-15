def checka(tab):
    for i in range(len(tab)-1):
        if abs(tab[i] - tab[i+1]) < 2:
            return False
    return True
def checkb(tab):
    #cyfry pierwsze: 2,3,5,7
    krota = (2,3,5,7)
    for i in range(len(tab)-1):
        if tab[i] in krota and tab[i+1] in krota:
            return False
    return True
def reku(tab,index,index_liczb):
    if index+1 == len(tab):
        if checka(tab) and checkb(tab):
            print(tab)
            return 1
        return 0
    suma = 0
    for i in range(len(tab)):
        if tab[i] == 0:
            tab[i] = index_liczb
            suma += reku(tab,index+1,index_liczb+1)
            tab[i] = 0
    return suma

t = [0 for _ in range(9)]
t[0] = 1
print(reku(t,0,2))
