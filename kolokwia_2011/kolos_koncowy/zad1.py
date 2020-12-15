#1. Mamy tablicę [1..max,1..max]. 
#Napisz funkcję, która zwraca długość najdłuższego podciągu rosnącego
#znajdującego się w dowolnym (jednym) wierszu, 
#którego wszystkie elementy są ze sobą względnie pierwsze.

def nwd(n1,n2):
    return n2 if n1==0 else nwd(n2%n1,n1)
def func(tab):
    n = len(tab)
    max_dl = 0
    for i in range(n):
        for j in range(n):
            a0 = tab[i][j]
            index_strt = j
            dl = 1
            for idx in range(j+1,n):
                if tab[i][idx] > a0:
                    for idx2 in range(index_strt,idx):
                        if nwd(tab[i][idx],tab[i][idx2]) != 1:
                            print(tab[i][idx],tab[i][idx2])
                            break
                    else:
                        print(tab[i][idx],dl+1)
                        dl+=1
                        a0 = tab[i][idx]
                        continue
                    break
                else:
                    if dl > max_dl:
                        max_dl = dl
            else:
                if dl > max_dl:
                    max_dl = dl
    return max_dl
print(func([[11,13,17,19],[11,15,3,5],[4,9,2,1],[7,6,5,4]]))
