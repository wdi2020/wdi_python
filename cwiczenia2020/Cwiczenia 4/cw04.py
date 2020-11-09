def cw04(MAX,t):
    col_sum = [0 for _ in range(MAX)]
    row_sum = [0 for _ in range(MAX)]
    for i in range(MAX):
        for j in range(MAX):
            row_sum[i] += t[i][j]
            col_sum[i] += t[j][i]
    col_max = col_sum[0]
    col_ind = 0
    row_max = row_sum[0]
    row_ind = 0
    for i in range(1,MAX):
        if col_sum[i] > col_max:
            col_max = col_sum[i]
            col_ind = i
        if row_sum[i] > row_max:
            row_max = row_sum[i]
            row_ind = i
    return (col_ind,row_ind) , col_max/row_max

if __name__ == "__main__":
    print(cw04(10,[[5 for _ in range(10)] for _ in range(10)]))
