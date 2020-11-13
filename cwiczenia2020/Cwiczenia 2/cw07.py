def wielokrotnosc():
    szukana = int(input(">:"))
    
    n = 1
    wyraz_ciagu = (n*n)+n+1

    while wyraz_ciagu < szukana:
        if szukana % wyraz_ciagu == 0:
            return True
        n += 1
        wyraz_ciagu = (n*n)+n+1
    if wyraz_ciagu == szukana:
        return True
    return False

if __name__ == "__main__":
    print(wielokrotnosc())
