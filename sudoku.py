#sudoku trywialna treść

def reku(tab,i,j,row_hash,col_hash,square_hash):
    if j == len(tab):
        j = 0
        i+=1
    if i == len(tab):
        return True
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
    col_hash = [[False for _ in range(10)]for _ in range(10)]
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
a = strt(tab)
for elem in a:
    print(elem)