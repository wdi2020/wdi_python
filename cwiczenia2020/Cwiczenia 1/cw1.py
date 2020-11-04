from math import pi,sqrt

def cw1():
    a1 = 1
    a2 = 1
    while a1 < 10**6:
        print(a1)
        a1,a2 = a2,a1+a2

def cw2(target):
    best = target
    result_a = 0
    result_b = 0
    for a in range(1,target//2):
        for b in range(1,target//2):
            f0 = a
            f1 = b
            while(f0 + f1 <= target):
                new_number = f0 + f1
                if new_number == target and a+b < best:
                    result_a = a
                    result_b = b
                    best = a+b
                f0,f1 = f1,new_number
    return (f"ta pierwsza to {result_a} a ta druga to {result_b}")

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

def cw5(liczba=25):
    n = 2
    a = 1
    b = 123
    e = 0.00000000001
    while abs(b-a) >= e:
        b,a= (1/n)*((n-1)*a+(liczba/(a**(n-1)))),b
    return a,b

def funkcja(x):
    return x**x - 2020
def cw6():
    a = 0
    b = 10
    e = 0.000001
    while True:
      s = (a + b)/2
      if abs(funkcja(s)) <= e:
        break
      if funkcja(s)*funkcja(a) < 0:
        b = s
      else:
        a = s
    print(s)

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
    while n < (liczba*(0.5))+1:
        if liczba % n == 0:
            return "tak" 
        n+=1
    return "nie"

def cw9(liczba):
    for i in range(liczba//2,0,-1):
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
    maximum = 10**4
    for a in range(2,maximum+1):
        suma_a = 1
        for i in range(int(sqrt(a)),1,-1):
            if a % i == 0:
                suma_a += (a//i) + i
        suma_b = 1
        for i in range(int(sqrt(suma_a)),1,-1):
            if suma_a % i == 0:
                suma_b += (suma_a//i) + i
        if suma_b == a and suma_a < a:
            print(a, suma_a, "Są dobre ...")

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

def szereg(x,n):
        return ((-1)**n)*(x**(2*n))/silnia(2*n)
def cw14():
    x = 2*pi
    x_1 = 0
    x_2 = 12
    n = 0
    suma = 0
    while abs(x_1 - x_2) > 0.0000001:
        x_1,x_2 = x_2,szereg(x,n)
        suma += x_2
        print(suma)
        n += 1 
def cw15():
    return_value = (0.5)**(0.5)
    value_of_ret_val_bef = 2
    value_before = (0.5)**(0.5)
    e = 0.00000000001
    while abs(value_of_ret_val_bef-return_value) >= e:
        temp = ((0.5) + ((.5)*value_before))**(.5)
        value_of_ret_val_bef = return_value
        return_value *= temp 
        value_before = temp
    pi_value = 2.0/return_value
    return pi_value
def cw16():
    #working*
    maxymalna_wartosc:int = 0
    liczba = 0
    for i in range(2,10000+1):
        count = 0
        a_n = i
        while abs(a_n - 1.0) > 0.000000054:
            a_n = cw16_rek(a_n)
            count += 1
        if count > maxymalna_wartosc:
            maxymalna_wartosc = count
            liczba = i
    return maxymalna_wartosc,liczba
def cw16_rek(a_n):
    return (a_n%2)*(3*a_n + 1) + (1-a_n%2) *(a_n/2)
def cw17(a = 1, b=1):
    a1,a2 = a,b
    iloraz_1, iloraz_2 = 1.0,10101010101010101010.0
    while abs(iloraz_1 - iloraz_2) > 0.00000000001:
        a1,a2 = a2,a1+a2
        iloraz_1, iloraz_2 = iloraz_2,a2/a1
    return iloraz_2
def cw18(A=125.0):
    # hard to tell jak to zrobic
    n = 3
    a = 1
    b = 123
    e = 0.00000000001
    while abs(b-a) >= e:
        b,a= (1/n)*((n-1)*a+(A/(a**(n-1)))),b
    return a,b

def cw19():
    ret = 1.0
    curr_silnia = 1
    for i in range(1,1000+1):
        curr_silnia = curr_silnia * i
        ret += 1/(curr_silnia)
    return ret
def silnia(nr):
    ret = 1
    for i in range(2,nr+1):
        ret *= i
    return ret
def cw20():
    a_n = 20.0
    b_n = 30.0
    a_n, b_n = (a_n*b_n)**(0.5), (a_n+b_n)/2.0
    while abs(a_n - b_n) >  0.000000000001:
        a_n,b_n = (a_n*b_n)**(0.5),(a_n+b_n)/2.0
    return b_n
if __name__ == "__main__":
    print(cw19())
