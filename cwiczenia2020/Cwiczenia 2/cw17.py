#cw 17
from math import log
def funkcja(x : int):
    return x - ((x**x) -2020)/(((x**x)*log(x)) + (x**x))
def cw17():
    e = 1
    old = 0
    a = 1
    a = funkcja(a)
    while abs(a-old) > e:
        old,a = a,funkcja(a)
    print(a)
if __name__ == "__main__":
    cw17()