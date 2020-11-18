def cw5(number):
    counter = 1
    num = number
    while num > 10:
        counter += 1
        num = num // 10
    print(counter)
    while counter != 0:
        rekurencja(number,counter)
        counter-=1

        
def rekurencja(number, counter):
    num = number
    num_after = num//10**counter
    num_after *= 10**(counter-1)
    num = num%10**(counter-1)
    num = num + num_after
    if num % 7 == 0:
        print(num)
    copy = num
    counter_new = 1
    while num > 10:
        counter_new += 1
        num = num // 10
    if counter_new == 1:
        return False
    while counter_new > counter:
        rekurencja(copy,counter_new)
        counter_new-=1


if __name__ == "__main__":
    cw5(2315)