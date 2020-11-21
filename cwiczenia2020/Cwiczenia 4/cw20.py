#working now ;)
def cw20(t,N):
    max_sum = 0
    x,y,x2,y2 = 0,0,0,0
    for a in range(N):
        for b in range(N):
            sum1 = 0
            i = 0
            while i < N:
                if i != a:
                    sum1 += t[i][b]
                if i !=b:
                    sum1 += t[a][i]
                i+=1
            for k in range(N):
                for l in range(N):
                    if k==a and l==b:
                        continue
                    sum2 = 0
                    if k == a:
                        sum2 += t[a][b]
                    else:
                        i = 0
                        while i < N:
                            if i != b and i != l:
                                sum2 += t[k][i]
                            i+=1
                    if l == b:
                        sum2 += t[a][b]
                    else:
                        i = 0
                        while i < N:
                            if i != a and i != k:
                                sum2 += t[i][l]
                            i+=1
                    if sum1+sum2>max_sum:
                        max_sum = sum1+sum2
                        x,y,x2,y2=a,b,k,l

    return (x,y),(x2,y2)

from random import randint
if __name__ == "__main__":
    st =[[randint(1,2) for _ in range(8)] for _ in range(8)] 
    #w głowie działa
    # st = [[999991,1,1,1],[2,0,0,0],[3,3,9,0],[1,5,121234,5]]
    # st = [[2, 2, 1],[2, 1, 2],[2, 2, 2]]
    # st = [[0, 1, 1],[0, 1, 1],[1, 0, 1]]
    # st = [[1, 1, 0],[0, 0, 0],[0, 0, 0]]
    st = [[0, 1, 0],[0, 1, 1],[1, 1, 1]]
    for i in st:
        print(i)
    print(cw20(st,len(st)))
