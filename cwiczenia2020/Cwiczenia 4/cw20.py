#not even fcking working .....
def cw20(t,N):
    r = 0
    sumy_col = [0 for _ in range(N)] 
    sumy_row = [0 for _ in range(N)] 
    i = 0
    while i<N:
        j=0
        while j<N:
            sumy_col[j] += t[i][j]
            sumy_row[i] += t[i][j]
            j+=1
        i+=1
    print(sumy_col,sumy_row)
    max_sum = 0
    x,y,x2,y2 = 0,0,0,0
    for a in range(N):
        for b in range(N):
            copy_col = sumy_col.copy()
            copy_row = sumy_row.copy()
            sum1=(copy_col[b]-t[a][b]) + (copy_row[a]-t[a][b])
            if a == 0 and b == 2:
                print(copy_col,copy_row)
            copy_col[b]=t[a][b]
            copy_row[a]=t[a][b]
            if a == 0 and b == 2:
                print(copy_col,copy_row)
            for k in range(N):
                for l in range(N):
                    if k==a and l==b:
                        continue
                    sum2=(copy_col[l]-t[k][l]) + (copy_row[k]-t[k][l])
                    if sum1+sum2>max_sum:
                        max_sum = sum1+sum2
                        x,y,x2,y2=b,a,l,k

    print(max_sum)
    return (max_sum),(x,y),(x2,y2)

from random import randint
if __name__ == "__main__":
    st =[[randint(1,2) for _ in range(8)] for _ in range(8)] 
    #w głowie działa
    st = [[999991,1,1,1],[2,0,0,0],[3,3,9,0],[1,5,121234,5]]
    st = [[2, 2, 1],[2, 1, 2],[2, 2, 2]]
    st = [[0, 1, 1],[0, 1, 1],[1, 0, 1]]
    st = [[1, 1, 0],[0, 0, 0],[0, 0, 0]]
    # st = [[0, 1, 0],[0, 1, 1],[1, 1, 1]]
    for i in st:
        print(i)
    print(cw20(st,len(st)))
