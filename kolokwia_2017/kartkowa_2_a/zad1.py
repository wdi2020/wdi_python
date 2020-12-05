# 2 wieze
def check(tab,r1,c1,r2,c2):
    if c1 ==c2 and r1==r2:
        return 0
    n = len(tab)
    suma = 0
    for i in range(n):
        #1-col
        if i != r2 and i != r1:
            suma += tab[r1][i]
        elif i == r2 and c2 == c1:
            suma += tab[i][c2]
        #2-col
        if i != r1 and i != r2:
            suma += tab[r2][i]
        elif i == r1 and c1 == c2:
            suma += tab[i][c1]
        #1-row
        if i != c2 and i != c1:
            suma += tab[i][r1]
        elif i == c1 and r1 == c2:
            suma += tab[r1][i]
        #2-row
        if i != c1 and i != c2:
            suma += tab[i][r2]
        elif i == c2 and r2 == c1:
            suma += tab[r2][i]
    return suma
def move(tab,n,c1,c2,r1,r2,max_sum):
    for i in range(n):
        if suma(tab,i,c1,r2,c2) > max_sum:
            return True
        if suma(tab,r1,i,r2,c2) > max_sum:
            return True
        if suma(tab,r1,c1,i,c2) > max_sum:
            return True
        if suma(tab,r1,c1,r2,i) > max_sum:
            return True
#jezeli funckja check dziala to to zadziala...
