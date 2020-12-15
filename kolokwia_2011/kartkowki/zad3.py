def is_prime(num):
    if num <= 1:
        return False
    if num==2 or num==3:
        return True
    if num%2==0 or num%3==0:
        return False
    i =5
    while i**2 <= num:
        if num%i==0 or num%(i+2):
            return False
        i+=6
    return True
def A(num,n):
    if n == 0:
        return ""
    num+=3
    if is_prime(num):
        return "A"
    a = A(num,n-1)
    if a != "":
        return "A"+a
    b = B(num,n-1)
    if b != "":
        return "A"+b
    c = C(num,n-1)
    if c != "":
        return "A"+c
    return ""

def B(num,n):
    if n == 0:
        return ""
    num*=2
    if is_prime(num):
        return "B"
    a = A(num,n-1)
    if a != "":
        return "B"+a
    b = B(num,n-1)
    if b != "":
        return "B"+b
    c = C(num,n-1)
    if c != "":
        return "B"+c
    return ""
def C(num,n):
    if n == 0:
        return ""
    #opercajcda
    cp = num
    cnt = 0
    while cp != 0:
        cp//=10
        cnt+=1
    if cnt == 1:
        return ""
    else:
        ost = num%10
        przed = (num%100)//10
        num//=100
        num*=100
        num += ost*10
        num += przed
    if is_prime(num):
        return "C"
    a = A(num,n-1)
    if a != "":
        return "C"+a
    b = B(num,n-1)
    if b != "":
        return "C"+b
    c = C(num,n-1)
    if c != "":
        return "C"+c
    return ""
#w glowie dziala
#ale jak jest tego nikt nie wie
