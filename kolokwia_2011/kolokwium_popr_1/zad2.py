def iprime(num):
    if num <= 1:
        return False
    if num ==2 or num ==3:
        return True
    if num%2==0 or num%3==0:
        return True
    i = 5
    while i*i<=num:
        if num%i==0 or num%(i+2)==0:
            return False
        i+=6
    return True

def fun(num):
    def reku(num,new_liczba,idx):
        if num==0:
            if new_liczba > 9 and idx != len(str(new_liczba)):
                print(new_liczba)
            return
        reku(num//10,new_liczba,idx+1)
        fi = (new_liczba//(10**(idx+1)))//10
        sec = new_liczba%(10**(idx))
        new_liczba  = fi+sec
        reku(num//10,new_liczba,idx)
    reku(num,num,0)
fun(2137)
