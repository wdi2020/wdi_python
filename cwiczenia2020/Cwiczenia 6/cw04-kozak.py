ruchY = ((-1,2),(1,2),(-1,-2),(1,-2),(-2,-1),(-2,-1),(2,1),(2,-1))
def jump_(tab,i,j,counter_strike):
    global ruchY
    tab[i][j] = True
    if counter_strike == 1: return True
    for elem in ruchY: 
        if i+elem[0] >= 0 and i+elem[0] < len(tab) and j+elem[1] >= 0 and j+elem[1] < len(tab) and tab[i+elem[0]][j+elem[1]] == False and jump_(tab,i+elem[0],j+elem[1],counter_strike-1): return True
    tab[i][j] = False
def start(dim):
    for i in range((dim+1)//2):
        for j in range(i,(dim+1)//2):
            if jump_([[False for _ in range(dim)]for _ in range(dim)],i,j,dim**2): return True

from time import time
sta = time()
print(start(5))
print(time()-sta)