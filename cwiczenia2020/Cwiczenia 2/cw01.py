def liczba_z_iloczynu():
    szukana = int(input("Podaj liczbe... "))

    a1,a2 = 1,1
    while True:
        if a2 > szukana:
            return False

        b1,b2 = 1,1
        while a2*b2 < szukana:
            b1,b2 = b2,b1+b2

        if a2*b2 == szukana:
            return True

        a1,a2 = a2, a1+a2
    
from time import time
if __name__ == "__main__":
    start = time()
    print(liczba_z_iloczynu())
    print(time() - start)