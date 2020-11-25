def rekur(sum,k,curr_row,tab,droga,idx,min_sum):
    sum += tab[curr_row][k]
    droga[idx] = k
    idx+=1
    if curr_row+1 == len(tab):
        if min_sum == -1 or sum < min_sum:
            min_sum = sum
        return min_sum 
    #end if
    if k >0:
        #lewo
        a = rekur(sum,k-1,curr_row+1,tab,droga,idx,min_sum)
        if min_sum == -1 or a < min_sum:
            min_sum = a
    if k+1 < len(tab):
        #prawo
        a = rekur(sum,k+1,curr_row+1,tab,droga,idx,min_sum)
        if min_sum == -1 or a < min_sum:
            min_sum = a
    #w dol
    a = rekur(sum,k,curr_row+1,tab,droga,idx,min_sum)
    if min_sum == -1 or a < min_sum:
        min_sum = a
    return min_sum 
#end def
def func(tab,k):
    #lewo, dol i prawo
    droga_ = [0 for _ in range(len(t))]
    return rekur(0,k,0,tab,droga_,0,-1)


t = [[1,1,1,1,1,1,1],[1,3,1,1,1,1,1],[4,1,1,1,1,1,1],[1,5,1,1,1,1,1],[1,1,1,1,1,1,1],[1,1,1,1,1,1,1],[1,1,1,1,1,1,1]]
t = [[10,1,10,10,10,10,10,10], [10,10,1,10,10,10,10,10],[10,1,10,10,10,10,10,10],[10,10,1,10,10,10,10,10],[10,1,10,10,10,10,10,10],[10,10,1,10,10,10,10,10],[10,10,1,10,10,10,10,10],[10,1,10,10,10,10,10,10]]
print(func(t,1))
for e in t:
    print(e)
