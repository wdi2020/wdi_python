def cw19(N,t):
    m = 0

    i = 0
    while i < N-1:
        j = i+1
        suma = 0
        suma_index = 0
        temp = t[i] 
        count = 0
        while j <N:
            if t[j] > temp:
                suma += t[j]
                suma_index += j
                temp = t[j]
                if suma == suma_index:
                    count+=1
                    if count > m:
                        m = count
                j+=1
            else:
                break
        i+=1
    return m
from random import randint
if __name__ == "__main__":
    print(cw19(50,[randint(1,5) for _ in range(50)]))