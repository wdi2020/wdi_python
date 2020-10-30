def cw04(MAX,t):
    col_sum = [0 for _ in range(MAX)]
    row_sum = [0 for _ in range(MAX)]
    for i in range(MAX):
        for j in range(MAX):
            row_sum[i] += t[i][j]
            col_sum[i] += t[j][i]
    iloraz_max = 0
    odp = (1,1)
    for i in range(MAX):
        for j in range(MAX):
            temp = col_sum[j] / row_sum[i]
            if temp > iloraz_max:
                iloraz_max = temp
                odp = (i,j)
    return odp,iloraz_max

if __name__ == "__main__":
    print(cw04(10,[[5 for _ in range(10)] for _ in range(10)]))
    
        
