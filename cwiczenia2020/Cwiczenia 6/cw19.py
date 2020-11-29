def can_move(tab,from_col,from_row,to_col,to_row,gdzie_byl,target_row,target_col):
    to_ = 0
    from_ = 0
    if to_col >= 0 and to_col <= 7 and to_row >= 0 and to_row <= 7:
        to_ = tab[to_row][to_col]
        from_ = tab[from_row][from_col]
        if gdzie_byl[to_row][to_col] == 1:
            return False
    else:
        return False
    if from_%10 < int(str(to_)[0]) and max(abs(target_col-from_col),abs(target_row-from_row)) >= max(abs(target_col-to_col),abs(target_row-to_row)):
        return True
    return False

def rekur(row,column,tab,gdzie_byl:list,target_row,target_col):
    gdzie_byl[row][column] =1
    if row == target_row  and column == target_col:
        return True
    ruchy = ((1,1),(1,0),(0,1),(1,-1))
    for elem in ruchy:
        if can_move(tab,column,row,column+elem[1],row+elem[0],gdzie_byl,target_row,target_col):
            if rekur(row+elem[0],column+elem[1],tab,gdzie_byl,target_row,target_col):
                return True
        if can_move(tab,column,row,column-elem[1],row-elem[0],gdzie_byl,target_row,target_col):
            if rekur(row-elem[0],column-elem[1],tab,gdzie_byl,target_row,target_col):
                return True
    gdzie_byl[row][column] =0
    return False
def func(tab,target_row,target_col):
    empty = [[0 for _ in range(8)] for _ in range(8)]
    a = rekur(0,0,tab,empty,target_row,target_col)
    return a

from random import randint
tab = [[91 for _ in range(8)] for _ in range(8)]
print(func(tab,3,4))
