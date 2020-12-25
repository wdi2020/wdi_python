# 1. Dana jest tablica wypełniona liczbami naturalnymi:
# const int N=1000; int t[N][N];
# Proszę napisać funkcję, która poszukuje w tablicy kwadratu o liczbie pól będącej liczbą nieparzystą
# większą od 1, którego iloczyn 4 pól narożnych wynosi k. Do funkcji należy przekazać tablicę i wartość
# k. Funkcja powinna zwrócić informacje czy udało się znaleźć kwadrat oraz współrzędne (wiersz,
# kolumna) środka kwadratu.

def check(row, col, wielkosci, k, tab):
    return tab[row][col] * tab[row + wielkosci][col + wielkosci] \
           * tab[row][col + wielkosci] * tab[row + wielkosci][col] == k


def func(tab, k, n=1000):
    for row in range(n):
        for col in range(n):
            if tab[row][col] > k:
                continue
            for wielkosci in range(3, min(n - row, n - col), 2):
                if check(row, col, wielkosci, k, tab):
                    return (2 * row + wielkosci) // 2, (2 * col + wielkosci) // 2

#w glowie dziala