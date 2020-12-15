#II kartkówka - TABLICE (grupa b)
#- dana jest 2-wymiarowa tablica integer, 
#znajdź element dla którego suma elementów leżących na
#przekątnych na których przecięciu znajduje się nasz element jest 
#największa

def in_buond(i,j,n):
    return i>=0 and i<n and j>=0 and j<n

def suma_prze(tab,i,j):
    suma = 0
    i_cp,j_cp = i,j
    while in_buond(i_cp,j_cp,len(tab)):
        suma += tab[i_cp][j_cp]
        i_cp-=1
        j_cp-=1
    i_cp,j_cp = i,j
    while in_buond(i_cp,j_cp,len(tab)):
        suma += tab[i_cp][j_cp]
        i_cp+=1
        j_cp+=1
    i_cp,j_cp = i,j
    while in_buond(i_cp,j_cp,len(tab)):
        suma += tab[i_cp][j_cp]
        i_cp-=1
        j_cp+=1
    i_cp,j_cp = i,j
    while in_buond(i_cp,j_cp,len(tab)):
        suma += tab[i_cp][j_cp]
        i_cp+=1
        j_cp-=1
    return suma

def meth(tab):
    row,col = 0,0
    max_val = 0
    for i in range(len(tab)):
        for j in range(len(tab)):
            if suma_prze(tab,i,j)>max_val:
                max_val = max(max_val,suma_prze(tab,i,j))
                row,col = i,j
    return row,col