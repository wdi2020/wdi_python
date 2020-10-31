def func(t,MAX):
    sum_max = 0
    row,col = 0,0
    i= 0
    while i<MAX: 
        j = 0
        while j<MAX:
            suma =0
            #prawo
            if j != MAX-1:
                suma += t[i][j+1]
            #lewo
            if j!=0:
                suma+= t[i][j-1]
            #dol
            if i!= MAX-1:
                suma+=t[i+1][j]
            #gora
            if i!= 0:
                suma+=t[i-1][j]
            if suma>sum_max:
                sum_max = suma
                row,col = i,j
            j+=1
        i+=1
    return row,col

from random import randint
if __name__ == "__main__":
    MAX = 100
    print(func([[randint(1,100) for _ in range(MAX)]for _ in range(MAX)],MAX))