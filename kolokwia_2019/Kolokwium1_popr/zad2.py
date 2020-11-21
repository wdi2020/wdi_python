#(a,b) b>a to klocek jakis mag-mino najlepsza gra
def rekur(tab,pomocnicza,dlugosc,curr,ostatni_tryb):
    #ostatni tryb to 1 (a) lub 0 (b)
    if False not in pomocnicza:
        return dlugosc
    i = 0
    for elem in tab:
        if pomocnicza[i] != True:
            dl = 0
            e = 0
            if ostatni_tryb == 1:
                e = 0
            else: 
                e = 1
            if elem[0] == curr[e]:
                pomocnicza[i] = True
                dlugosc+=1
                dl = rekur(tab,pomocnicza,dlugosc,elem,0)
                dlugosc-=1
                pomocnicza[i] = False
            if elem[1] == curr[e]:
                pomocnicza[i] = True
                dlugosc+=1
                dl2 = rekur(tab,pomocnicza,dlugosc,elem,1)
                dlugosc-=1
                pomocnicza[i] = False
            else:
                continue
            if dl > dlugosc:
                dlugosc = dl
            if dl2 > dlugosc:
                dlugosc = dl2
        i+=1
    return dlugosc
    
def func(tab):
    #tab to lista klockow ( (a,b) )
    max_dl = 0
    pomocnicza = [False for _ in range(len(tab))]
    i = 0
    for elem in tab:
        pomocnicza[i] = True
        dl = rekur(tab,pomocnicza,1,elem,0)
        dl2 = rekur(tab,pomocnicza,1,elem,1)
        max_dl = max(dl,dl2,max_dl)
        pomocnicza[i] = False
        i+=1
    return (max_dl)

tablica = [(2,8),(0,1),(2,3),(3,6),(2,6),(2,9),(3,4),(6,7)]
print(func(tablica))
