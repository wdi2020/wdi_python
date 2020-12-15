#Zadanie 1.Dana jest tablica wypeªniona liczbami naturalnymi int t[N][N] reprezentuj¡ca szachownic¦.
#funkcj¦, która sprawdza, czy jest mo»liwe ustawienie dwóch wzajemnie szachuj¡cych si¦ skoczków tak, aby
#suma warto±ci pól, na których stoj¡ skoczki, byªa liczb¡ pierwsz¡. Do funkcji nale»y przekaza¢ tablic¦ t,
#funkcja powinna zwróci¢ warto±¢ typu bool.
def is_Prime(num):
    if num <=1:
        return False
    if num == 2 or num == 3:
        return True
    if num %2 ==0 or num%3 == 0 :
        return False
    i = 6
    while (i-1)**2 <num:
        if num%(i-1) == 0 or num %(i+1) == 0:
            return False
        i+=6
    return True
def can_be(row,col,n):
    if row >= 0 and col >= 0 and row<n and col<n:
        return True
    return False
def ustaw(tab,n):
    ruchy = (2,1),(1,2),(-1,2),(2,-1)
    for i in range(n):
        for j in range(n):
            for elem in ruchy:
                if can_be(i+elem[0],j+elem[1],n):
                    if is_Prime(tab[i][j] + tab[i+elem[0]][j+elem[1]]):
                        return True
                if can_be(i-elem[0],j-elem[1],n):
                    if is_Prime(tab[i][j] + tab[i-elem[0]][j-elem[1]]):
                        return True
    return False
