def func(t,n):
    max_sum = 0
    cop,cop2 = 0,0
    for i in range(n):
        for j in range(n):
            sum1 = 0
            k = 0
            while k <n:
                sum1+=t[i][k]
                sum1+=t[k][j]
                k+=1
            sum1-= t[i][j]
            if i == 0 and j == 0:
                print(sum1)
            for k in range(n):
                for l in range(n):
                    if k == i and l == j:
                        continue
                    sum2 = 0
                    m = 0
                    if k != i:
                        while m < n:
                            if m != j and j != l:
                                sum2+=t[k][m]
                            m+=1
                    m = 0
                    if l != j:
                        while m<n:
                            if i != m and i != k:
                                sum2+=t[m][l]
                            m+=1
                    if k != i and l != j:
                        sum2-=t[k][l]
                    if sum1+sum2 > max_sum:
                        max_sum = sum1+sum2
                        cop = (i,j)
                        cop2 = (k,l)
    return max_sum,cop,cop2

print(func([[1,0,0],[1,1,0],[1,1,1]],3))