#tablica 9 na 9 aka sudoku niepowtarzacajace sie w wierszach i kolumnach i 9-9
#ruch skoczka w sensie niepowtarzac sie
# kazdy wiersz musi tworzyc liczbe pierwsza w systemie 2 z reszt z dzielenia przez 2 elementów w komórkach
#zakres 0-9


#ruch skoczka w sensie niepowtarzac sie
def check_skoczek(tab):
    def can_move(x,y):
        if x >= 0 and x < len(tab) and y>= 0 and y< len(tab):
            return True
        return False
    ruchy = ((1,2),(1,-2),(2,1),(2,-1))
    n = len(tab)
    for i in range(n):
        for j in range(n):
            for elem in ruchy:
                if can_move(i+elem[0],j+elem[1]):
                    if tab[i][j] == tab[i+elem[0]][j+elem[1]]:
                        return False
    return True


# kazdy wiersz musi tworzyc liczbe pierwsza w systemie 2 z reszt z dzielenia przez 2 elementów w komórkach
def check_wiersz(tab):
    def to_binary(num):
        t = []
        while num != 0:
            t.insert(0,num%2)
            num//=2
        ret  = 0
        for elem in t:
            ret *=10
            ret += elem
        return ret
    def czy_pierwsza(num):
        if num <=1:
            return False
        if num==2 or num==3:
            return True
        if num%2==0 or num%3==0:
            return False
        i = 5
        while i*2 <= num:
            if num%i==0 or num%(i+2)==0:
                return False
            i+=6
        return True
    for row in tab:
        suma  = 0
        for elem in row:
            suma += elem
        if not czy_pierwsza(to_binary(suma)):
            return False

def reku(tab,i,j,row_hash,col_hash,square_hash):
    if j == len(tab):
        j = 0
        i+=1
    if i == len(tab):
        if check_skoczek(tab):
            return True
        return False
    if tab[i][j] != 0:
        if reku(tab,i,j+1,row_hash,col_hash,square_hash):
            return True
        return False
    for num in range(1,10):
        if row_hash[i][num] == True or col_hash[j][num] == True or square_hash[i//3][j//3][num] == True:
            continue
        row_hash[i][num] = True
        col_hash[j][num] = True
        square_hash[i//3][j//3][num] = True
        tab[i][j] = num
        if reku(tab,i,j+1,row_hash,col_hash,square_hash):
            return True
        tab[i][j] = 0
        row_hash[i][num] = False
        col_hash[j][num] = False 
        square_hash[i//3][j//3][num] = False
    return False

def strt(tab):
    col_hash = [[False for _ in range(10)] for _ in range(10)]
    row_hash = [[False for _ in range(10)] for _ in range(10)]
    square_hash = [[[False for _ in range(10)] for _ in range(3)] for _ in range(3)]
    for i in range(len(tab)):
        for j in range(len(tab)):
            if tab[i][j] == 0:
                continue
            col_hash[j][tab[i][j]] = True
            row_hash[i][tab[i][j]] = True
            square_hash[i//3][j//3][tab[i][j]] = True
    reku(tab,0,0,row_hash,col_hash,square_hash)
    return tab

tab = [[0 for _ in range(9)]for _ in range(9)]

from time import time
start = time()
a = strt(tab)
print(time()-start)

for elem in a:
    print(elem)