#10**6
#slow 
def czy_pierwsza(num):
    if num == 1:
        return False
    if num == 2:
        return True
    if num %2 == 0:
        return False
    i = 3
    while i*i <= num:
        if num%i == 0:
            return False
        i+=2
    return True

def get_dzielnik_suma(num):
    suma = 0
    if num % 2 ==0:
        while num % 2 == 0:
            suma += 2
            num //= 2
    if num %3 == 0:
        while num %3 == 0:
            suma += 3
            num //= 3
    if czy_pierwsza(num):
        return num
    i = (num//2)+1 
    while num > 1 and i >1:
        if num %i == 0:
            if czy_pierwsza(i):

                copy = i
                if copy < 10:
                    suma += copy
                else:
                    while copy != 0:
                        suma += copy%10
                        copy//=10
            else:
                suma += get_dzielnik_suma(i)

            if czy_pierwsza(num // i):
                
                copy = num // i
                if copy < 10:
                    suma += copy
                else:
                    while copy != 0:
                        suma += copy%10
                        copy//=10

            else:
                suma += get_dzielnik_suma(num//i)
            break
        i -= 1

    return suma
            
    
def cw16(parameter):
    i = 4
    while i <= parameter:
        suma_cyfr = 0
        copy = i
        while copy > 0:
            suma_cyfr += copy%10
            copy //= 10
        if not czy_pierwsza(i):
            if get_dzielnik_suma(i) == suma_cyfr:
                print(i) 
        i += 1

from time import time
if __name__ == "__main__":
    start = time()
    print(cw16(100000))
    print(time() - start)