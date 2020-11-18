def cw05(MAX,t):
    col_sum = [0 for _ in range(MAX)]
    row_sum = [0 for _ in range(MAX)]
    for i in range(MAX):
        for j in range(MAX):
            row_sum[i] += t[i][j]
            col_sum[i] += t[j][i]
    iloraz_max =0 
    odp = (0,0)
    for i in range(1,MAX):
        for j in range(1,MAX):
            if row_sum[i] == 0:
                continue
            temp = col_sum[j] / row_sum[i]
            if temp >= iloraz_max:
                iloraz_max = temp
                odp = (i,j)
    return odp,iloraz_max

from  random import randint
if __name__ == "__main__":
    t = [[randint(-2,2) for _ in range(10)] for _ in range(10)]
    for i in t:
        print(i)
    print()
    print(cw05(10,t))