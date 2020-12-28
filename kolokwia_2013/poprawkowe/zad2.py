# 2. Napisz procedurę, która jako argument przyjmuje liczbę całkowitą i wypisuje wszystkie co najmniej
# dwucyfrowe liczby pierwsze, powstale poprzez wykreślenie z liczby pierwotnej co najmniej jednej cyfry.
def is_prime(num):
    if num <= 1:
        return False
    if num == 2 or num == 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i ** 2 <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True


def wypisz_je(num):
    def reku(pierwsza, num, wykresolen: bool, idx):
        if pierwsza==0:
            if num >= 10 and wykresolen:
                if is_prime(num):
                    print(num)
            return
        # end if
        reku(pierwsza//10, num, wykresolen, idx + 1)
        num = (num // (10 ** (idx + 1))) * 10 ** idx + num % (10 ** idx)
        reku(pierwsza//10, num, True, idx)

    reku(num, num, False,0)

wypisz_je(2137)
