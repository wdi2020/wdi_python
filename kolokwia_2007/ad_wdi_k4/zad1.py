#1. Dany jest typ tablicowy mapa = array [ 1..max,1..max ] of Boolean;
#reprezentujący mapę. Wartość true oznacza ląd, a wartość false ocean. 
#Na
#oceanie znajdują się wyspy utworzone przez sąsiadujące pola (rysunek).
#Proszę
#napisać w Pascalu funkcję do której 
# przekazujemy mapę i współrzędne x,y
#punktu na mapie. Jeżeli współrzędne oznaczają punkt na wyspie, funkcja
#powinna zatopić wyspę. 
#Funkcja powinna zwrócić rozmiar zatopionego obszaru.
#Można założyć, że żadna wyspa na mapie nie styka się z jej krawędzią.

def can_take(i,j,tab):
    if i<0 or j<0 or i>=len(tab) or j>=len(tab):
        return False
    if tab[i][j] == True:
        return True
    return False
#otoczka
def func(tab,row,col):
    if tab[row][col] == False:
        return 0
    cnt = 1
    is_empty = True
    k = 1
    while True:
        if is_empty==True:
            return cnt
        for i in range(-k,k+1):
            if can_take(row-k,col+i,tab):
                cnt+=1
                is_empty= False
            if can_take(row+k,col+i,tab):
                cnt+=1
                is_empty= False
            if can_take(row+i,col-k,tab):
                cnt+=1
                is_empty = False
            if can_take(row+i,col+k,tab):
                cnt+=1
                is_empty = False
        k+=1
#to nie dziala, na wiki jest dzialajaca wersja