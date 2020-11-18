#author - Nikodem K.
N = int(input("podaj liczbe: "))
e = 1
a = 1
sil = 1
t = [0 for i in range(10000)]
t[0] = 1
kon = False
while not kon:
    sil *= a
    n = 1
    licz = 0
    for x in range(N+3):
        if (n//sil) % 10 == 0:
            licz += 1
        if licz - 3 == N:
            kon = True
        t[x] += (n//sil) % 10
        n *= 10
        if t[x] > 9:
            t[x] %= 10
            t[x-1] += 1
    a += 1
print(t[0], end='.')
for x in range(1, N+1):
    print(t[x], end="")

