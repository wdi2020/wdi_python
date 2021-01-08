# 1. Dwie liczby naturalne są „przyjaciółkami” jeżeli zbiory cyfr z których zbudowane są liczby
# są identyczne. Na przykład: 123 i 321, 211 i 122, 35 i 3553. Dana jest tablica int t[N][N]
# wypełniona liczbami naturalnymi. Proszę napisać funkcję, która dla tablicy t zwraca ile
# elementów tablicy sąsiaduje wyłącznie z przyjaciółkami.

def check(tab1, tab2):
    for i in range(10):
        if tab1[i] != tab2[i] and (tab1[i] == 0 or tab2[i] == 0):
            return False
    return True


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

