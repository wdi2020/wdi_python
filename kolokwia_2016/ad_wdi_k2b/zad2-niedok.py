#Dana jest tablica int t[N][N] (reprezentująca szachownicę) wypełniona liczbami naturalnymi.
#W każdej kolumnie znajduje się dokładnie jedna wieża, której numer wiersza zawiera tablica
#int w[N]. Proszę napisać funkcję która wybiera do usunięcia z szachownicy dwie wieże, tak aby
#suma liczb na polach szachowanych przez pozostałe wieże była najmniejsza. Do funkcji należy
#przekazać tablice t i w, funkcja powinna zwrócić numery kolumn z których usunięto wieże.
#Uwagi:
#    - zakładamy, że wieża szachuje cały wiersz i kolumnę z wyłączeniem pola na którym stoi
def suma(c1,r1,r2,c2,t,N,ile_w_row,w,suma_col_):
    sumaa = 0
    sumaa += suma_col[c1]
    sumaa -= tab[r1][c1]



def ile_w_rpow(w,N):
    pohash = [0 for _ in range(N)]
    i = 0
    for elem in w:
        col = i
        row = elem
        pohash[row] +=1
        i+=1
    return pohash
def suma_col(t,N):
    suma_column=[0 for _ in range(N)]
    i=0
    while i<N:
        j=0
        while j<N:
            suma_column[j] += tab[i][j]
            j+=1
        i+=1
    return suma_column

def iter(t,w):
    N = len(t)
    dl_wiez = len(w)
    suma_col_ = suma_col(t,N)
    ilosc_w_row = ile_w_rpow(w,N)
    max_usun = 0
    col1,col2= 0,0
    for i in range(dl_wiez):
        for j in range(i+1,dl_wiez):
            a = suma(i,w[i],j,w[j],t,N,ilosc_w_row,w,suma_col_)
            if a> max_usun:
                max_usun = a
                col1,col2 = i,j
    return col1,col2
