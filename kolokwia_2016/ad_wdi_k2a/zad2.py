#Dana jest tablica t[N][N] (reprezentująca szachownicę) wypełniona liczbami naturalnymi.
#Proszę napisać funkcję która ustawia na szachownicy dwie wieże, tak aby suma liczb na
#„szachowanych” przez wieże polach była największa. Do funkcji należy przekazać tablicę,
#funkcja powinna zwrócić położenie wież.
#Uwagi:
#    - zakładamy, że wieża szachuje cały wiersz i kolumnę z wyłączeniem pola na którym stoi
#
def sumy(r1,c1,r2,c2,tab):
    #tu bylaby suma ale juz ja pisalem z 5 razy
def func(tab):
    maxym = 0
    for i in range(len(tab)):
        for j in range(len(tab)):
            for k in range(len(tab)):
                for l in range(len(tab)):
                    if i==k and j==l:
                        continue
                    a = sumy(i,j,k,l,tab)
                    if a > maxym:
                        maxym = a
    return maxym
