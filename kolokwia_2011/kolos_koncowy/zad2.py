#2. Mamy dany zbiór punktów.
#tab=array[1..max] of punkt;
#Napisz funkcję, która zwróci 
#najmniejszą odległość między środkami ciężkości 2 
#niepustych podzbiorów tego zbioru.

#krotka typu (x,y)

def check(t1,t2,idx1,idx2):
    if idx1 == 0 or idx2==0:
        return -1

    sum1 = [0,0]
    for i in range(idx1):
        elem = t1[i]
        sum1[0] += elem[0]
        sum1[1] += elem[1]

    sum2 = [0,0]
    for i in range(idx2):
        elem = t2[i]
        sum2[0] += elem[0]
        sum2[1] += elem[1]

    sum1[0]/=idx1
    sum1[1]/=idx1

    sum2[0]/=idx2
    sum2[1]/=idx2

    dl = ((sum1[0] - sum2[0])**2 + (sum2[1]-sum1[1])**2)**.5
    return dl
def reku(tab,idx,t1,t2,idx1,idx2,max_value):
    if idx == len(tab):
        a = check(t2,t2,idx1,idx2)
        if max_value == -1:
            return a
        if a < max_value and a != -1:
            return a
        return max_value
    max_value = reku(tab,idx+1,t1,t2,idx1,idx2,max_value)
    t1[idx1] = tab[idx]
    max_value = reku(tab,idx+1,t1,t2,idx1+1,idx2)
    t2[idx2] = tab[idx]
    max_value = reku(tab.idx+1,t1,t2,idx1,idx2+1,max_value)
    return max_value
#should work
