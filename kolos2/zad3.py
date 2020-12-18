#opis:
#mój algorytm na poczatku wpisuje do 2 tablic pomocniczych sume wierszy i kolumn
#nastepnie przechodzi po kazdej mozliwej kombinacji 2 wiez i sprawdza czy suma ich ustawien będzie najwieksza
#funkcja zlicz wieze zlicza sume pod obiema wiezami
def zlicz_wieze(row1,row2,col1,col2,t,sumy_wiersz,sumy_kolumny):
    suma=0
    suma =sumy_wiersz[row1] + sumy_wiersz[row2] + sumy_kolumny[col1] + sumy_kolumny[col2] 
    suma -= 2*t[row1][col1]
    suma -= 2*t[row2][col2]
    if col1 == col2:
        suma -= sumy_kolumny[col1]
    elif row1 == row2:
        suma -= sumy_wiersz[row1]
    else:
        suma -= t[row1][col2] 
        suma -= t[row2][col1]
    return suma
def chess(T):
    n=len(T)
    max_suma =0
    r1,r2,c1,c2=0,0,0,0
    suma_kolumn=[0 for _ in range(n)]
    suma_wierszy=[0 for _ in range(n)]
    for i in range(n):
        for j in range(n):
            suma_kolumn[i] += T[j][i]
            suma_wierszy[i] += T[i][j]
    for row1 in range(n):
        for col1 in range(n):
            for row2 in range(row1+1,n):
                for col2 in range(col1+1,n):
                    suma = zlicz_wieze(row1,row2,col1,col2,T,suma_wierszy,suma_kolumn)
                    if suma>max_suma:
                        r1,c1,r2,c2=row1,col1,row2,col2
                        max_suma=suma
    return r1,c1,r2,c2
