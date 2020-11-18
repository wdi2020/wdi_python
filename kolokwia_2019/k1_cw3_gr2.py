from random import randint
def rekurencja_3_1(t,poprzedni_hetman,N, suma,row):
    if row == N :
        if suma == 0:
            print("dziala")
            return True
        else:
            return False
    for i in range(N):
        if i == poprzedni_hetman:
            continue
        elif i+1 == poprzedni_hetman and i+1 != N:
            continue
        elif i-1 == poprzedni_hetman and i-1 != -1:
            continue
        else:
            suma += t[row][i]
            rekurencja_3_1(t,i,N,suma,row+1)
N = 6
t = [[randint(-1,1) for _ in range(N)] for _ in range(N)]
rekurencja_3_1(t,-5,N,0,0)
