def func(t,q,MAX):
    count =0
    i = 0
    while i<MAX:
        j = 0
        while j<MAX:
            if i>=2:
                if j>=1:
                    if t[i][j] * q == t[i-2][j-1]:
                        count+=1
                if j<=MAX-2:
                    if t[i][j] * q == t[i-2][j+1]:
                        count+=1
            if i<=MAX-3:
                if j>=1:
                    if t[i][j] * q == t[i+2][j-1]:
                        count+=1
                if j<=MAX-2:
                    if t[i][j] * q == t[i+2][j+1]:
                        count+=1
            if j>=2:
                if i>=1:
                    if t[i][j] * q == t[i-1][j-2]:
                        count+=1
                if i<=MAX-2:
                    if t[i][j] * q == t[i+1][j-2]:
                        count+=1
            if j<=MAX-3:
                if i>=1:
                    if t[i][j] * q == t[i-1][j-2]:
                        count+=1
                if i<=MAX-2:
                    if t[i][j] * q == t[i+1][j-2]:
                        count+=1
            j+=1
        i+=1
    return count

from random import randint
if __name__ == "__main__":
    MAX = 1000
    print(func([[randint(1,10000) for _ in range(MAX)] for _ in range(MAX)],5,MAX))