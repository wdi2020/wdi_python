# Kolos 1 z 2019/2020 ~Łukasz Pawlak

from random import randint
def zad1():
    t1= [randint(0,600) for _ in range(50)]
    t2 = [randint(0,600) for _ in range(50)]
    t1= [1 for _ in range(50)]
    t2 = [1 for _ in range(50)]
    print(t1)
    print(t2)
    for i in range(50):
        for j in range(50):
            for k in range(0,25):
                if len(t1) - i - k < 0:
                    continue
                if len(t2) - 24 - j + k < 0:
                    continue
                temp1 = t1[i:k:1]
                temp2 = t2[j:24-k:1]
                sum1 = 0
                sum2 = 0
                for i in temp1:
                    sum1 += i
                for i in temp2:
                    sum2 += i
                if cw4(sum1 + sum2):
                    print(f"ta {sum1 + sum2}")
                    return None
    print("nie")
def cw4(searched_number):
    podstawa = 2
    sum = podstawa
    while True:
        sum = podstawa * podstawa
        if sum > searched_number:
            return False
        while sum <= searched_number:
            if sum == searched_number:
                return True 
            sum *= podstawa
        podstawa += 1
def zad2():
    t1= [[randint(0,600) for i in range(50)] for j in range(50)]
    # t1= [[0 for i in range(50)] for j in range(50)]
    tru = False
    for i in range(50):
        if tru == True:
            break
        for j in range(50):
            tru = False
            temp = t1.copy()
            for k in range(50):
                if tru == True:
                    break
                if k == i:
                    continue
                for l in range(49):
                    if tru == True:
                        break
                    if j == l or l == j+1:
                        continue
                    buuff = 0
                    odd_numbers = 0
                    while True:
                        if temp[k][l] == 1 :
                            odd_numbers += 1
                            break
                        elif temp[k][l] == 0:
                            break
                        else: 
                            buuff = temp[k][l] % 2
                            temp[k][l] //= 2
                            if buuff == 1:
                                odd_numbers += 1
                    if odd_numbers % 2 != 1:
                        tru = True
                        break
                if tru == True:
                    break
            if tru == True:
                continue
            print(temp,i,j)
            return "Działa"
            
def zad3():
    N = 8
    tablica = [[randint(-10,10) for _ in range(N)] for _ in range(N)]
    print(rekurencja_3(tablica,0,0,-5,-5,N))
def rekurencja_3(tablica,suma,row,krol_pierwszy,krol_drugi,N):
    if row == N and suma == 0:
        print("jg")
        return True
    elif row == N:
        return False
    for i in range(N):
        roznica = krol_pierwszy - i
        if roznica < 0:
            roznica *= -1
        if roznica <= 2:
            continue
        roznica = krol_drugi - i
        if roznica < 0:
            roznica *= -1
        if roznica <= 2:
            continue
        suma = suma + tablica[row][i]
        rekurencja_3(tablica,suma,row+1,krol_drugi,i,N)
    return False

def zad1_1():
    N = 8
    t1 = [randint(1,100) for _ in range(N)] 
    t2 = [randint(1,100) for _ in range(N)] 
    for i in range(1,N):
        for j in range(0,N-i):
            for k in range(0,N-i):
                sums = 0
                temp1 = t1[j:j+i]
                temp2 = t2[k:k+i] 
                for number in temp1:
                    sums+= number
                for number in temp2:
                    sums+= number
                dividers = zad1_1_is_prime(sums)
                if dividers == -1 :
                    continue
                elif len(dividers) == 2:
                    print()
                    if zad1_1_is_prime(dividers[0]) == [dividers[0]] and zad1_1_is_prime(dividers[1]) == [dividers[1]]:
                        print(f"Jest, działa z {temp1} i  z {temp2}")
                        return None
def zad1_1_is_prime(num):
    no_of_dividers = []
    if num > 1:
        i = 2
        while num  > 1:
            if num == 1:
                break
            if num % i == 0:
                print(num)
                no_of_dividers.append(i)
                num = num // i
                i = 2
                continue
            i += 1
        return no_of_dividers
    else:
        return -1
def zad2_1():
    N = 8
    t1= [[randint(0,600) for i in range(N)] for j in range(N)]
    t1= [[8 for i in range(N)] for j in range(N)]
    tru = False
    for i in range(N):
        if tru == True:
            break
        for j in range(N):
            tru = False
            for k in range(N):
                if tru == True:
                    break
                if k == i:
                    continue
                for l in range(N-1):
                    if tru == True:
                        break
                    if j == l or l == j+1:
                        continue
                    podstawa = 2
                    while podstawa ** 2 <= t1[k][l]:
                        potega = 2
                        while podstawa ** potega < t1[k][l]:
                            i = 2
                            while True:
                                if i * (podstawa**potega) <= t1[k][l]:
                                    if  i * (podstawa**potega) == t1[k][l]:
                                        return "TAK"
                                    i += 1
                                else:
                                    break
                            potega += 1
                        podstawa += 1
                    return "brak mozliwosci"
def zad3_1():
    N = 6
    t = [[randint(-1,1) for _ in range(N)] for _ in range(N)]
    rekurencja_3_1(t,-5,N,0,0)

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
            

if __name__ == "__main__":
    zad3_1()