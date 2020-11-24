def can_move(tab,from_col,from_row,to_col,to_row):
    to_ = 0 
    from_ = 0 
    if to_col >= 0 and to_col < 7 and to_row >= 0 and to_row < 7:
        to_ = tab[to_row][to_col]
        from_ = tab[from_row][from_col]
    else:
        return False
    if from_%10 < int(str(to_)[0]) and max(abs(7-from_col),abs(7-from_row)) >= max(abs(7-to_col),abs(7-to_row)):
        return True
    return False

def rekur(row,column,tab,last_oper):
    if row == 7 and column == 7:
        return True
    #gora
    if can_move(tab,column,row,column,row-1) and last_oper != 5:
        if rekur(row-1,column,tab,0):
            return True
    #prawo gora
    if can_move(tab,column,row,column+1,row-1) and last_oper != 6:
        if rekur(row-1,column+1,tab,1):
            return True
    #lewo gora
    if can_move(tab,column,row,column-1,row-1) and last_oper != 7:
        if rekur(row-1,column-1,tab,2):
            return True
    #prawo
    if can_move(tab,column,row,column+1,row) and last_oper != 4:
        if rekur(row,column+1,tab,3):
            return True
    #lewo
    if can_move(tab,column,row,column-1,row) and last_oper != 3:
        if rekur(row,column-1,tab,4):
            return True
    #dol
    if can_move(tab,column,row+1,column,row) and last_oper != 0:
        if rekur(row+1,column,tab,5):
            return True
    #lewo dol
    if can_move(tab,column,row+1,column-1,row) and last_oper != 1:
        if rekur(row+1,column-1,tab,6):
            return True
    #prawo dol
    if can_move(tab,column,row+1,column+1,row) and last_oper != 2:
        if rekur(row+1,column+1,tab,7):
            return True
    return False
def func(tab):
    return rekur(0,0,tab,0)

from random import randint
tab = [[randint(81,9000) for _ in range(8)] for _ in range(8)]
print(func(tab))
#chuj wie czy dziala jakby ktos mial jakis test to prosze wyslac, w glowie sie kompiluje
# a i chodzenie 1,4,5 czyli prawo gora,lewo dol ale nw o co im chodzi bo to nie ma prawa dzialac 