# 1. Dwie liczby naturalne są „koleżankami” jeżeli mają przynajmniej dwie różne wspólne cyfry,
# np. 123 i 1345 lub 225 i 1235. Dana jest tablica t[N][N] wypełniona liczbami naturalnymi.
# Proszę napisać funkcję, która w tablicy t zeruje wszystkie liczby nie mające żadnej koleżanki.
# Do funkcji należy przekazać tablicę t. Funkcja powinna zwrócić ilość liczb naturalnych jaka
# pozostanie w tablicy.
def check(tab1, tab2):
    cnt = 0
    for i in range(10):
        if tab1[i] > 0 and tab2[i] > 0:
            cnt += 1
    return cnt >= 2


def zlicz(tab):
    n = len(tab)
    prev = [0 for _ in range(10)]
    curr = [0 for _ in range(10)]
    next = [0 for _ in range(10)]
    cnt = 0
    for i in range(0, n * n):
        if i % n == 0:
            curr = [0 for _ in range(10)]
            cp = tab[i // n][i % n]
            while cp != 0:
                curr[cp % 10] += 1
                cp //= 10
            next = [0 for _ in range(10)]
            cp = tab[(i + 1) // n][(i + 1) % n]
            while cp != 0:
                next[cp % 10] += 1
                cp //= 10
            if check(curr, next):
                cnt += 1
        elif i % n == n - 1:
            prev = curr
            curr = next
            if check(prev, curr):
                cnt += 1
        else:
            prev = curr
            curr = next
            next = [0 for _ in range(10)]
            cp = tab[i // n][(i + 1) % n]
            while cp != 0:
                next[cp % 10] += 1
                cp //= 10
            if check(prev, curr) and check(curr, next):
                cnt += 1
    return cnt
