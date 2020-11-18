#by sb
number = int(input("Podaj liczbę: "))
k = int(input("Podaj przedział: "))
n = int(input("Na ile prostokątów chcesz podzielić wykres: "))
a = (k - 1)/n
Summ = 0
center = 1 + (k-1)/2*n
i = 0


def funtion(a):
    return a*a+a+2


if number == 0:
    print("Musisz podac liczbę różną od 0.")
else:
    while i < k:
        Summ += funtion(center)
        center += a
        i += 1
    print(Summ*a)