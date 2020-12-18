#IV zadanie (5 punktów)
#- na liczbych naturalnych określono 3 rodzaje przekształceń:
#a:=a+1
#a:=3*a
#a:=a div 2 (tylko jeżeli liczba a jest parzysta)
#napisać w Pascalu program, który rozstrzyga czy jest mozliwe przekształcenie liczby a w b w serii
#przekształceń o długości nie większej od n, warości a,b,n nalezy wczytać z klawiatury,
#na przykład dla danych a=13 b=11 n=5 odpowiedz brzmi tak bo
#13->14->7->21->22->11
#dla danych a=13, b=6, n=5 odpowiedź brzmi nie 
def reka(a,b,n):
    if a ==b:
        return True
    if n ==0:
        return False
    a = a+1
    if reka(a,b,n-1) or rekb(a,b,n-1) or rekc(a,b,n-1):
        return True
    return False
def rekb(a,b,n):
    if a ==b:
        return True
    if n ==0:
        return False
    a = a*3
    if reka(a,b,n-1) or rekb(a,b,n-1) or rekc(a,b,n-1):
        return True
    return False
def rekc(a,b,n):
    if a ==b:
        return True
    if n ==0:
        return False
    if a%2==0 and a != 0:
        a//=2
    else:
        return False
    if reka(a,b,n-1) or rekb(a,b,n-1) or rekc(a,b,n-1):
        return True
    return False
def strt(a,b,n):
    if reka(a,b,n) or rekb(a,b,n) or rekc(a,b,n):
        return True
    return False
print(strt(13,6,5))
print(strt(13,11,5))