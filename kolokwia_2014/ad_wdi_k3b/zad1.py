# 1. Dana jest tablica wypełniona liczbami naturalnymi:
# const int N=1000;
# int t[N][N];
# Proszę napisać funkcję, która w poszukuje w tablicy najdłuższego ciągu geometrycznego leżącego ukośnie w kierunku
# prawo-dół, liczącego co najmniej 3 elementy. Do funkcji należy przekazać tablicę. Funkcja powinna zwrócić
# informacje czy udało się znaleźć taki ciąg oraz długość tego ciągu.

def func(tab, n=1000):
    q = -1
    curr_dl = 0
    max_dl = 2
    for col in range(n):
        row_cp = 0
        col_cp = col
        while row_cp < n - 1 and col_cp < n - 1:
            if q == -1:
                if tab[row_cp][col_cp] == 0:
                    continue
                q = tab[row_cp + 1][col_cp + 1] / tab[row_cp][col_cp]
                curr_dl = 2

            elif tab[row_cp][col_cp] * q == tab[row_cp + 1][col_cp + 1]:
                curr_dl += 1
            else:
                if curr_dl > max_dl:
                    max_dl = curr_dl
                    q = -1
            row_cp += 1
            col_cp += 1
    #zmiana planu tu druga czesc fora
        if col ==0:
            continue
        row_cp = col
        col_cp = 0
        while row_cp < n - 1 and col_cp < n - 1:
            if q == -1:
                if tab[row_cp][col_cp] == 0:
                    continue
                q = tab[row_cp + 1][col_cp + 1] / tab[row_cp][col_cp]
                curr_dl = 2

            elif tab[row_cp][col_cp] * q == tab[row_cp + 1][col_cp + 1]:
                curr_dl += 1
            else:
                if curr_dl > max_dl:
                    max_dl = curr_dl
                    q = -1
            row_cp += 1
            col_cp += 1

    if max_dl >2:
        return max_dl
    else:
        return 0

#standard w glowie dziala