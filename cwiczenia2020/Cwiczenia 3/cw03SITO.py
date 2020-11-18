n = int(input("daj  n:"))

tablica = [True for _ in range(n-1)]

for i in range(2,int(n**.5)+1):
    if tablica[i-2] == True:
        j = 2
        while True:
            i_j = j*i
            if i_j <= n:
                tablica[i_j-2] = False
            else: 
                break
            j += 1

for i in range(0,n-1):
    if tablica[i] == True:
        print(i+2,end=", ")
