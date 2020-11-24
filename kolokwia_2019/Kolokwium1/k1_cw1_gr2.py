from random import randint
def is_prime(num):
    no_of_dividers = []
    if num > 1:
        i = 2
        while num  > 1 and i <= (num)**(1/2):
            if num % i == 0:
                no_of_dividers.append(i)
                num = num // i
                i = 2
                continue
            i += 1
        if num > 1:
            no_of_dividers.append(num)
        return no_of_dividers
    else:
        return -1
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
            dividers = is_prime(sums)
            if dividers == -1 :
                continue
            elif len(dividers) == 2:
                print()
                if is_prime(dividers[0]) == [dividers[0]] and is_prime(dividers[1]) == [dividers[1]]:
                    print(f"Jest, działa z {temp1} i  z {temp2}")
                    exit(0) 