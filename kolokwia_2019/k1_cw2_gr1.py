from random import randint
t1= [[randint(0,600) for i in range(50)] for j in range(50)]
# t1= [[0 for i in range(50)] for j in range(50)]
tru = False
for i in range(50):
    if tru == True:
        break
    for j in range(50):
        tru = False
        temp = t1.copy()
        for k in range(50):
            if tru == True:
                break
            if k == i:
                continue
            for l in range(49):
                if tru == True:
                    break
                if j == l or l == j+1:
                    continue
                buuff = 0
                odd_numbers = 0
                while True:
                    if temp[k][l] == 1 :
                        odd_numbers += 1
                        break
                    elif temp[k][l] == 0:
                        break
                    else: 
                        buuff = temp[k][l] % 2
                        temp[k][l] //= 2
                        if buuff == 1:
                            odd_numbers += 1
                if odd_numbers % 2 != 1:
                    tru = True
                    break
            if tru == True:
                break
        if tru == True:
            continue
        print(temp,i,j)
        exit(0) 