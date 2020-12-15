#Zadanie 21. Tablica T[8][8] zawiera liczby naturalne. Proszę napisać funkcję, która sprawdza czy można
#wybrać z tablicy niepusty podzbiór o zadanej sumie. Warunkiem dodatkowym jest aby żadne dwa wybrane
#elementy nie leżały w tej samej kolumnie ani wierszu. Do funkcji należy przekazać wyłącznie tablicę oraz
#wartość sumy, funkcja powinna zwrócić wartość typu bool.
def t(tab):
    tab.append(1)
    return True
a = []
print(True or t(a))
print(a)
print(True|t(a))
print(a)