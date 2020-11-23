def czy_palindrom(tab):
    for i in range(len(tab)//2):
        if tab[i] != tab[len(tab)-1-i]:
            return False
    return True
def func(tab):
    max_dl = 0
    for i in range(len(tab)):
        for j in range(i+1,len(tab)):
            if tab[i] == tab[j]:
                for k in range(0,j-i):
                    brek = False
                    if tab[i+k] != tab[j-k]:
                        break
                    coop = tab[i+k]
                    while coop != 0:
                        if (coop%10)%2 == 0:
                            brek = True
                            break
                        coop//=10
                    coop = tab[j-k]
                    while coop != 0:
                        if (coop%10)%2 == 0:
                            brek = True
                            break
                        coop//=10
                    if brek == True:
                        break
                else:
                    if j-i+1 > max_dl :
                        max_dl = j-i+1
    return max_dl

n = 1000
t = [3 for _ in range(n)]
print(func(t))


