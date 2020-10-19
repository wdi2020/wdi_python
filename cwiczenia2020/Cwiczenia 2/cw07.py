def wielokrotnosc():
    szukana = int(input("Podaj liczbe naturalna uzywajac klawiatury a ja odpowiem czy jest wielokrotnoscia dowolnego wyrazu ciagu danego wzorem..."))
    
    n = 1
    wyraz_ciagu = (n*n)+n+1

    while wyraz_ciagu < szukana:
        mnoznik = 2
        while wyraz_ciagu * mnoznik < szukana:
            mnoznik += 1
        #end while
        if wyraz_ciagu * mnoznik == szukana:
            return True
        n += 1
        wyraz_ciagu = (n*n)+n+1
    return False

if __name__ == "__main__":
    print(wielokrotnosc())
