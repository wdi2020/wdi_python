#II kartkówka - TABLICE (grupa a)
#- dana jest 2-wymiarowa tablica integer, znajdź element 
#dla którego suma otaczających go elementów
#będzie największa


def suma(tab,i,j):
    def can_take(row,col):
        if row<0 or col<0 or row>=len(tab) or col>=len(tab):
            return 0
        return tab[i][j]
    suma = 0
    for row in range(i-1,i+2):
        for col in range(j-1,j+2):
            suma += can_take(row,col)
    return suma

def func(tab):
    max_sum = 0
    for i in range(len(tab)):
        for j in range(len(tab)):
            max_sum = max(max_sum,suma(tab,i,j))
    return max_sum