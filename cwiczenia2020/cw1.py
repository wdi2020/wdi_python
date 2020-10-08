#Cw1 - proste programy z pętlami cz 1 ~~lpawlak
from math import sqrt

def cw1():
    a1 = 1
    a2 = 1
    while a1 < 10**6:
        print(a1)
        new_number = a2+a1
        a1 = a2
        a2 = new_number

def cw2(target):
    best = target
    result_a =0
    result_b = 0
    for a in range(1,target//2):
        for b in range(1,target//2):
            f0 = a
            f1 = b
            while(f0 + f1 < target + 2):
                new_number = f0 + f1
                if new_number == target and a+b < best:
                    result_a = a
                    result_b = b
                    best = a+b
                f0 = f1
                f1 = new_number
    print(f"ta pierwsza to {result_a} a ta druga to {result_b}")

def cw3(searched_number):
    a1 : int = 1
    a2 : int = 1
    suma : int = 0
    b1 = 1
    b2 = 1
    while True:
        suma += a1
        if searched_number - suma == 0:
            return True
        if searched_number < suma:
            while True:
                if suma - b1 == searched_number:
                    return True
                if suma - b1 < searched_number:
                    return False
                suma -= b1
                new_number_b = b1 + b2
                b1 = b2
                b2 = new_number_b
        new_number = a1 + a2
        a1 = a2
        a2 = new_number


def cw4(searched_number):
    suma = 0
    ret = 1
    while True:
        suma += (2*ret - 1 )
        if suma == searched_number:
            return ret 
        if suma > searched_number:
            return ret-1
        ret += 1

def cw5(pole):
    dokladnosc :float = 0.01
    a,b = 1.,pole
    while abs(a-b) >= dokladnosc:
        a = (a+b)/2
        b = pole/a
    return a

def cw6_funkcja(x):
    return x**x -2020

def cw6():
    #co z ta bisekcja...
    return None

def cw7():
    liczba_szukana = int(input("Podaj liczbe:"))
    a1 = 1
    a2 = 1
    while a1 <= liczba_szukana // 2 :
        new_number = a2+a1
        a1 = a2
        a2 = new_number
        i = 1
        while a2 <= liczba_szukana:
            if new_number == liczba_szukana:
                return a2,i
            i+=1
            new_number = a2*i
    return "nie ma takiej liczby"

def cw8(liczba):
    if liczba % 2 == 0:
        return "tak"
    n = 3
    while n < liczba//2:
        if liczba % n == 0:
            return "tak" 
        n+=1
    return "nie"

def cw9(liczba):
    for i in range(liczba,0,-1):
        if liczba % i == 0:
            print(i)

def cw10():
    maximum = 10**6
    for a in range(4,maximum+1):
        suma = 0
        for i in range(a-1,0,-1):
            if a % i == 0:
                suma += i
        if suma == a:
            print(a, "Jest dobra")

def cw11():
    maximum = 10**5
    for a in range(2,maximum+1):
        suma_a = 0
        for i in range((a//2)+1,0,-1):
            if a % i == 0:
                suma_a += i
        suma_b = 0
        for i in range((suma_a//2)+1,0,-1):
            if suma_a % i == 0:
                suma_b += i
        if suma_b == a and suma_a != a:
            print(a, suma_a, "Są dobre ...") 
    return "zakończono"

def cw12(a =60,b=30,c=105):
    return min(nwd(a,b),nwd(a,c),nwd(b,c))

def nwd(a,b):
    while b != 0:
        b,a = a%b,b
    return a

def cw13():
    # nww = a*b*c / nwd
    a = 14
    b = 3
    c = 6
    nww_a_b = a*b//nwd(a,b)
    nww_a_c = a*c//nwd(a,c)
    nww_b_c = b*c//nwd(b,c)
    return max(nww_a_b,nww_a_c,nww_b_c)

def cw14():
    # tak szczerze to co to za typ...
    pass
def cw15():
    #for real?
    pass
def cw16():
    #not working
    maxymalna_wartosc:int = 0
    liczba = 0
    for i in range(2,10000+1):
        count = 0
        a_n = i
        while a_n - 1.0 > 0.000000054:
            a_n = cw16_rek(a_n)
            count += 1
        if count > maxymalna_wartosc:
            maxymalna_wartosc = count
            liczba = i
    return maxymalna_wartosc,liczba
def cw16_rek(a_n):
    return (a_n%2)*(3*a_n + 1) + (1-a_n%2) *(a_n/2)
def cw17(a = 1, b=1):
    #hard to tell czy dziala
    a1,a2 = a,b
    iloraz_1, iloraz_2 = 1.0,10101010101010101010.0
    while abs(iloraz_1 - iloraz_2) > 0.00000000001:
        a1,a2 = a2,a1+a2
        iloraz_1, iloraz_2 = iloraz_2,a2/a1
    return iloraz_2
def cw18():
    # patrz cw 5, (spoiler alert!)nie ma go
    pass
def cw19():
    ret = 1.0
    for i in range(1,1000+1):
        print(i)
        ret += 1/silnia(i)
    return ret
def silnia(nr):
    ret = 1
    for i in range(1,nr+1):
        ret *= i
    return ret
def cw20():
    a_n = 20.0
    b_n = 30.0
    a_n,b_n = sqrt(a_n*b_n),(a_n+b_n)/2.0
    while a_n - b_n >  0.000000000001:
        a_n,b_n = sqrt(a_n*b_n),(a_n+b_n)/2.0
    return b_n
if __name__ == "__main__":
    print(cw17())
