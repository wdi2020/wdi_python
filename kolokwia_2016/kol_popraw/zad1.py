#Dana jest tablica int t[N][N] zawierająca liczby naturalne. 
#Dokładnie w jednym wierszu, bądź kolumnie znajduje się fragmentu ciągu arytmetycznego o długości
#większej niż 2, którego elementy są liczbami pierwszymi. Proszę napisać funkcjęktóra zwróci długość tego ciągu.

def is_prime(num):
    if num <=1:
        return False
    if num ==2 or num == 3:
        return True
    if num %2 ==0 or num %3 == 0:
        return False
    i = 6
    while (i-1)**2 <= num:
        if num%(i-1) == 0 or num(i+1) == 0:
            return False
        i+=6
    return True
def strt(tab):
    dl = 2
    curr_dl = 2
    a0 = 0
    r = 0
    #to jest to co a0,r tylko ze do kolumn
    b0,l = 0,0
    curr_dl_kol = 0
    for i in range(len(tab)):
        for j in range(len(tab)):
            #wiersze
            if a0 != 0:
                if is_prime(tab[i][j]) and tab[i][j-1] + r == tab[i][j]:
                    curr_dl+=1
                else:
                    if curr_dl > dl:
                        dl = curr_dl
                    a0 = 0
                    r = 0
            if j != len(tab)-1 and a0 == 0:
                if is_prime(tab[i][j]) and is_prime(tab[i][j+1]):
                    a0 = tab[i][j]
                    r = tab[i][j+1] - a0
                    curr_dl = 1
            #kolumny
            if b0 != 0:
                if is_prime(tab[j][i]) and tab[j-1][i] + l == tab[j][i]:
                    curr_dl_kol+=1
                else:
                    if curr_dl_kol > dl:
                        dl = curr_dl_kol
                    b0 = 0
                    l = 0
            if j != len(tab)-1 and b0 == 0:
                if is_prime(tab[j][i]) and is_prime(tab[j+1][i]):
                    b0 = tab[j][i]
                    l = tab[j+1][i] - b0
                    curr_dl_kol = 1
    return dl

test = [[3,4,3,3],[3,4,3,6],[3,6,3,9],[3,3,3,9]]
print(strt(test))

