
#by vicioo
def ex19():
#Zadanie 19. Napisac program wczytujacy dwie liczby naturalne a,b i wypisujacy rozwiniecie dziesietne
#ułamka a/b w postaci ułamka okresowego. Na przykład 1/3 = 0.(3), 1/6 = 0.1(6), 1/7 = 0.(142857)

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