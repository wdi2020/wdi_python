def cw15():
    liczba = input("Podaj liczbe za chwile bd magia... :")
    return not liczba[-1:] in liczba[:-1]

def cw15_nudna_wersja():
    liczba = int(input("Podaj nudna liczbe.."))
    last = 0
    last = liczba %10
    liczba //= 10
    while liczba != 0:
        if last == liczba%10:
            return False
        liczba //= 10 
    return True

if __name__ == "__main__":
    print(cw15())