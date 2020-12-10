#2. Dane są dwie tablice mogące pomieścić taką samą liczbę elementów:
# int t1[10][N];
# int t2[M]; // M = 10*N
#W każdym wierszu tablicy t1 znajdują się uporządkowane rosnąco (w obrębie wiersza) liczby
#naturalne.
#Proszę napisać fragment programu przepisujący wszystkie singletony (liczby występujące dokładnie
#raz) z tablicy t1 do t2, tak aby liczby w tablicy t2 były uporządkowane rosnąco. Pozostałe elementy
#tablicy t2 powinny zawierać zera.

def sprawdz_min(tab,idx):
    for i in range(0,10):
        if i == idx:
            continue
        if tab[idx] == tab[i]:
            return False
    return True
def znajdz_min(tab):
    idx = 0
    minimum = tab[0][0]
    while minimum == -1 and idx < len(tab):
        idx+=1
        minimum =t[idx][0]
    for i in range(10):
        if tab[i][0] < minimum and tab[i][0] != -1:
            idx = i
            minimum = tab[i][0]
    if minimum == -1 and idx == len(tab):
        return -1
    return idx
def strt(tab):
    t2 = [0 for _ in range(10*len(tab[0]))]
    t2_idx = 0
    idx = znajdz_min(tab)
    while idx != -1:
        if sprawdz_min(tab,idx):
            print(t2_idx,idx)
            t2[t2_idx] = tab[idx][0]
            t2_idx +=1
        else:
            if len(tab[idx]) != 1:
                tab[idx].pop(0)
            else:
                tab[idx][0] = -1
        idx = znajdz_min(tab)
    return t2


n = 5
t1 = [[2 for j in range(n)] for i in range(10)]
print(strt(t1))
