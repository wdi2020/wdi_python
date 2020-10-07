#Cw1 - proste programy z pętlami cz 1 ~~lpawlak
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
    while True:
        suma += a1
        if searched_number - suma == 0:
            return True
        if searched_number < suma:
            b1 = 1
            b2 = 1
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
            return "Nie ma"
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



if __name__ == "__main__":
    print(cw10())