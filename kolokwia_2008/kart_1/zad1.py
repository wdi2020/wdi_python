#prosze napisac program wczytujacy liczby naturalne (wieksze od 10) 
#i odpowiedziec na pytanie czy w liczbie bedacej suma wczytanych liczb 
#cyfry ulkozone sa rosnaca. Na przyklad 13411 i 68 -> tak
#25000 i 57 -> nie
def func():
    s = "podaj liczbe >10 :"
    num1 = int(input(s))
    if num1 <= 10:
        num1 = 0
    while num1 <= 10:
        num1 = int(input(s))
        if num1 <= 10:
            num1 = 0
    num2 = int(input(s))
    if num2 <= 10:
        num2 = 0
    while num2 <= 10:
        num2 = int(input(s))
        if num2 <= 10:
            num2 = 0
    #liczby wczytane
    num = num1+num2
    a0 = 10
    while num != 0:
        if num%10 >= a0:
            return "Nie"
        a0 = num%10
        num//=10
    return "Tak"

print(func())