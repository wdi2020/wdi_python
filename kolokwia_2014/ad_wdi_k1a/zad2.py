#2. Dane są dwie tablice mogące pomieścić taką samą liczbę elementów:
# int t1[N][N];
# int t2[M]; // M = N*N
#W każdym wierszu tablicy t1 znajdują się uporządkowane niemalejąco (w obrębie wiersza) liczby
#naturalne. Proszę napisać fragment programu przepisujący wszystkie liczby z tablicy t1 do t2, tak aby
#liczby w tablicy t2 były uporządkowane niemalejąco.
n = 10
t1 = [[i+(j+n) for i in range(n)]for j in range(n)]
t2 = [0 for _ in range(n*n)]
wyznacznik = 0
min_curr = t1[0][0]
for i in range(1,n):
    if t1[i][0] < min_curr:
        min_curr = t1[i][0]
        wyznacznik = i
idx = 0
while True:
    t2[idx] = min_curr
    if len(t1[wyznacznik]) == 1:
        t1[wyznacznik] = [-1]
    else:
        t1[wyznacznik].pop(0)
    idx+=1
    if idx == n*n:
        break
    wyznacznik = 0
    min_curr = t1[0][0]
    while min_curr == -1:
        wyznacznik += 1
        min_curr = t1[wyznacznik][0]
    for i in range(wyznacznik+1,n):
        if t1[i][0] < min_curr and t1[i][0] != -1:
            min_curr = t1[i][0]
            wyznacznik = i
print(t2)
