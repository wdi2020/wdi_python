def cw17(N):
    N -= 1
    liczba = 10**N
    while liczba < 10**(N+1):
        suma = 0
        copy = liczba
        while copy > 0:
            suma += (copy%10)**(N+1)
            copy//=10
        if liczba == suma:
            print(liczba)
        liczba += 1

if __name__ == "__main__":
    cw17(6)
