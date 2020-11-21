def nwd(a,b):
    while b != 0:
        b,a = a%b,b
    return a 
def func(tab):
    n = len(tab)
    i = 0 
    while i <n:
        j = 0
        while j+1 < n:
            print(j)
            if nwd(tab[i][j],tab[i][j+1]) != 1:
                j+=1
                continue
            k = 0
            while k+1 < n:
                l = 0
                while l <n:
                    if i == k or k+1 == i or j == l or j+1 == l:
                        l+=1
                        continue
                    if nwd(tab[k][l],tab[k+1][l]) != 1:
                        l+=1
                        continue
                    if nwd(tab[i][j],tab[k][l]) != 1 or nwd(tab[i][j+1],tab[k][l]) != 1 or nwd(tab[i][j],tab[k+1][l]) != 1 or nwd(tab[i][j+1],tab[k+1][l]) != 1:
                        l+=1
                        continue
                    return True
                    l+=1
                k+=1
            j+=1
        i+=1
    return False

from random import randint
n = 8
t = [[777 for _ in range(n)] for _ in range(n)]
print(func(t))