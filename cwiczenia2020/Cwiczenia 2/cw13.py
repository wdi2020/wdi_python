def cw13():
    liczba = input("Podaj liczbe :")
    return not liczba[-1:] in liczba[:-1]

def cw13_nudna_wersja():
    liczba = int(input("Podaj liczbe.."))
    last = 0
    last = liczba %10
    liczba //= 10
    while liczba != 0:
        if last == liczba%10:
            return False
        liczba //= 10 
    return True

if __name__ == "__main__":
    print(cw13())