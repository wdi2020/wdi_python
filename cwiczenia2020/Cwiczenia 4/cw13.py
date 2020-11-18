def czy_pierwsza(num):
    if num <=1:
        return False
    if num ==2 or num ==3:
        return True
    if num %2==0 or num%3==0:
        return False
    i = 6
    while (i-1)**2<=num:
        if num %(i-1) == 0:
            return False
        if num%(i+1) == 0:
            return False
        i+=6
    return True

#bruteforce
def cw13(t):
    i = 0
    while i<len(t):
        j = 0
        while j<len(t):
            k,h = 0,0
            is_there = False
            while k <len(t):
                h = 0
                while h<len(t):
                    if (k != i and h!= j) and czy_pierwsza(t[i][j]+t[k][h]) and t[k][h] != 0:
                        is_there = True
                        break
                    h+=1
                if is_there:
                    break
                k+=1
            if not is_there:
                t[i][j] = 0
            j+=1
        i+=1
    return t
from random import randint
if __name__ == "__main__":
    print(cw13([[((j*10)+i) for i in range(10)] for j in range(10)]))
