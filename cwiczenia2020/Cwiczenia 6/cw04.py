#kon
def rekur(tab,y,x):
    tab[y][x] = True
    i = y
    j = x
    # prawo gora --^
    if i >= 1 and j <= len(tab)-3:
        if tab[y-1][x+2] != True:
            if rekur(tab,i-1,j+2):
                return True
    #prawo dol --v
    if i <= len(tab)-2 and j <= len(tab)-3:
        if tab[y+1][x+2] != True:
            if rekur(tab,i+1,j+2):
                return True
    #lewo gor --^
    if i >= 1 and j >= 2:
        if tab[y-1][x-2] != True:
            if rekur(tab,i-1,j-2):
                return True
    #lewo dol --v
    if i<=len(tab)-3 and j>=2:
        if tab[y+1][x-2] != True:
            if rekur(tab,i+1,j-2):
                return True
    #gora prawo ||>
    if i-2 >= 0 and j+1 <= len(tab)-1:
        if tab[y-2][x+1] != True:
            if rekur(tab,i-2,j+1):
                return True
    #gora lewo ||<
    if i-2 >= 0 and j-1 >= 0:
        if tab[y-2][x-1] != True:
            if rekur(tab,i-2,j-1):
                return True
    #dol prawo ||>
    if i+2 <= len(tab)-1 and j+1 <= len(tab)-1:
        if tab[y+2][x+1] != True:
            if rekur(tab,i+2,j+1):
                return True
    #dol lewo ||<
    if i+2 <= len(tab)-1 and j-1 >= 0:
        if tab[y+2][x-1] != True:
            if rekur(tab,i+2,j-1):
                return True

    e = 0
    for elem in tab:
        for column in elem:
            if column == False:
                e =1
                break
        if e == 1:
            break
    else:
        return True
    tab[y][x] = False
def func(n):
    for i in range((n+1)//2):
        for j in range(i,(n+1)//2):
            tab = [[False for _ in range(n)]for _ in range(n)]
            if rekur(tab,i,j):
                return True
    return False 

from time import time
start = time()
print(func(6))
print(time()-start)
