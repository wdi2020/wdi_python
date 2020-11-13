
#https://github.com/Viciooo/WDI_zestawy
def ex19():

    a, b = map(int, input().split())
    first_a = -1
    spaces = max(factorize(b, 2), factorize(b, 5))
    print(a//b, end='.')

    a %= b
    while True:
        cnt = 0
        while a < b:
            a *= 10
            cnt += 1

        if cnt > 1:
            print(0, end='')

        if a == first_a:
            break

        if spaces == 0:
            print('(', end='')
            first_a = a

        print(a//b, end='')
        a %= b
        spaces -= 1

    print(')')

def factorize(n, factor):
    cnt = 0
    while n % factor == 0:
        n //= factor
        cnt += 1
    return cnt