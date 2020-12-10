#Dana jest tablica booli int t[N][N] reprezentująca szachownicę. 
#Pole szachownicy ma wartość true, jeżeli stoi na nim figura, a false, jeśli jest ono puste. 
#Proszę napisaćfunkcję która sprawdza czy istnieje droga skoczka przemieszczającego się z 
#wiersza 0 do wiersza N-1. Skoczek może poruszać się tylko po polach pustych. 
#Skoczek wkażdym ruchu powinien przybliżać się do N-1 wiersza. 
#Funkcja ma zwrócić najmniejszą możliwą liczbę ruchów. 
#Skoczek może zacząć poruszać się z dowolnego pustego pola z wiersza 0. N z zakresu 4...20.

def can_move(tab,row,col,n):
    if row >= 0 and col >= 0 and row < n and col < n:
        if tab[row][col] == False:
            return True
    return False

def reku(tab,n,row,col,ilosc_ruchow):
    min_ilosc = n
    if row == n-1:
        return ilosc_ruchow
    ruchy = (1,2),(1,-2),(2,1),(2,-1)
    for elem in ruchy:
        if can_move(tab,row+elem[0],col+elem[1],n):
            a =  reku(tab,n,row+elem[0],col+elem[1],ilosc_ruchow+1)
            if a < min_ilosc:
                min_ilosc = a
    return min_ilosc

def strt(tab):
    n = len(tab)
    min_ilosc = n
    i = 4
    while i <= 20 and i < n:
        a =  reku(tab,n,0,i,0)
        if a < min_ilosc:
            min_ilosc = a
        i+=1
    return False
# w glowei dziala