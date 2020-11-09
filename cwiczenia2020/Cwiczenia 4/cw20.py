#not even fcking working .....
def cw20(t,N):
    sumy_col = [0 for _ in range(N)] 
    sumy_row = [0 for _ in range(N)] 
    i = 0
    while i<N:
        j=0
        while j<N:
            sumy_col[j] += t[i][j]
            sumy_row[i] += t[j][i]
            j+=1
        i+=1
    max_col = 0
    max_row = 0
    x,y = 0,0
    i = 1
    while i<N:
        j = 0
        while j<N:
            if sumy_col[j]-t[i][j] > max_col:
                max_col = sumy_col[j]-t[i][j]
                x=j
            if sumy_row[i]-t[i][j] > max_row:
                y=i
                max_row = sumy_row[i]-t[i][j]
            j+=1
        i+=1
    sumy_col[x] = t[y][x] 
    sumy_row[y] = t[y][x] 

    max_col = 0
    max_row = 0
    x2,y2 = 0,0
    i = 1
    while i<N:
        j = 0
        while j<N:
            if sumy_col[j]-t[i][j] > max_col:
                max_col = sumy_col[j]-t[i][j]
                x2=j
            if sumy_row[i]-t[i][j] > max_row:
                y2=i
                max_row = sumy_row[i]-t[i][j]
            j+=1
        i+=1
    return (max_col + max_row),(x,y),(x2,y2)

from random import randint
if __name__ == "__main__":
    st =[[randint(1,2) for _ in range(8)] for _ in range(8)] 
    #w głowie działa
    st = [[999991,1,1,1],[2,0,0,0],[3,3,9,0],[1,5,121234,5]]
    st = [[2, 2, 1],[2, 1, 2],[2, 2, 2]]
    st = [[0, 1, 1],[0, 1, 1],[1, 0, 1]]
    st = [[1, 1, 0],[0, 0, 0],[0, 0, 0]]
    for i in st:
        print(i)
    print(cw20(st,len(st)))
