min_sum = -1
droga_min = []
def rekur(sum,k,curr_row,tab,droga):
    sum += tab[curr_row][k]
    droga.append(k)
    if curr_row+1 == len(tab):
        global min_sum
        global droga_min
        if min_sum == -1 or sum < min_sum:
            min_sum = sum
            droga_min = tuple(droga)
        droga.pop()
        return None
    #end if
    if k >0:
        #lewo
        rekur(sum,k-1,curr_row+1,tab,droga)
    if k+1 < len(tab):
        #prawo
        rekur(sum,k+1,curr_row+1,tab,droga)
    #w dol
    rekur(sum,k,curr_row+1,tab,droga)
    droga.pop()
    return None
#end def
def func(tab,k):
    #lewo, dol i prawo
    rekur(0,k,0,tab,[])


t = [[1,1,1,1,1,1,1],[1,3,1,1,1,1,1],[4,1,1,1,1,1,1],[1,5,1,1,1,1,1],[1,1,1,1,1,1,1],[1,1,1,1,1,1,1],[1,1,1,1,1,1,1]]
func(t,0)
print(min_sum,droga_min)