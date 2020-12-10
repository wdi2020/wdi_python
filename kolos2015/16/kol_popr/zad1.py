def func(tab):
    max_dl = 2
    nr_wiersza = 0
    curr_dl = 0
    c0,c1 = 1,1
    flag =False
    for i in range(len(tab)):
        for j in range(len(tab)):
            if j == 0:
                flag = False
                if curr_dl > max_dl:
                    nr_wiersza = i-1
                    max_dl = curr_dl
                curr_dl = 0
            if flag:
                c0,c1 = c1,c0+c1
                if c0 != tab[i][j]:
                    flag = False
                    if curr_dl > max_dl:
                        nr_wiersza = i
                        max_dl = curr_dl
                    continue
                else:
                    curr_dl+=1
                    flag = True
            else:
                c0,c1 = 1,1
                while c0 < tab[i][j]:
                    c0,c1 = c1,c0+c1
                if c0 != tab[i][j]:
                    continue
                else:
                    curr_dl=1
                    flag = True
    return nr_wiersza

t1 = [[5,3,6],[1,1,2],[3,7,4]]
print(func(t1))