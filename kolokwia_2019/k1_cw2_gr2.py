from random import randint

N = 8
t1= [[randint(0,600) for _ in range(N)] for _ in range(N)]
# t1= [[8 for i in range(N)] for j in range(N)]
tru = False
for i in range(N):
    if tru == True:
        break
    for j in range(N):
        tru = False
        for k in range(N):
            if tru == True:
                break
            if k == i:
                continue
            for l in range(N-1):
                if tru == True:
                    break
                if j == l or l == j+1:
                    continue
                podstawa = 2
                while podstawa ** 2 <= t1[k][l]:
                    potega = 2
                    while podstawa ** potega < t1[k][l]:
                        i = 2
                        while True:
                            if i * (podstawa**potega) <= t1[k][l]:
                                if  i * (podstawa**potega) == t1[k][l]:
                                    print("da się")
                                    exit(0)
                                i += 1
                            else:
                                break
                        potega += 1
                    podstawa += 1
print("nie da sie")