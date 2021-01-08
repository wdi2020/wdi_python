# 1. Mamy tablicę [1..max,1..max] of integer. Wyzeruj w niej wszystkie liczby które nie mają w tablicy innej
# liczby, która powstałaby poprzez przestawienie jej cyfr. (uważając na 1000 i 0100 - nie dziala).

def suun(tab):
    # ile cyfr
    def ile_cyfr(num):
        if num == 0:
            return 0
        import math
        return math.floor(math.log10(num) + 1)

    n = len(tab)
    checked = [[False for _ in range(n)] for _ in range(n)]
    for i in range(n ** 2):
        if checked[i // n][i % n] == True:
            continue
        cnt_i = ile_cyfr(tab[i // n][i % n])
        pomoc_i = [0 for _ in range(10)]
        cp = tab[i // n][i % n]
        while cp != 0:
            pomoc_i[cp % 10] += 1
            cp //= 10
        flag = True
        for j in range(i + 1, n ** 2):
            cnt_j = ile_cyfr(tab[j // n][j % n])
            if cnt_j != cnt_i:
                continue
            pomoc_j = [0 for _ in range(10)]
            cp = tab[j // n][j % n]
            while cp != 0:
                pomoc_j[cp % 10] += 1
                cp //= 10
            for k in range(1, 10):
                if pomoc_j[k] != pomoc_i[k]:
                    break
            else:
                checked[j // n][j % n] = True
                checked[i // n][i % n] = True
                flag = False
        else:
            if flag == True:
                tab[i // n][i % n] = 0


tab = [[123, 2, 3], [123, 45, 32], [6, 321, 54]]
for i in tab:
    print(i)
suun(tab)
for i in tab:
    print(i)
