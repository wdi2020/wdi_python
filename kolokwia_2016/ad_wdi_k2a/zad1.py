def rozklad(a):
    ret = []
    i = 2
    while a != 1:
        if a % i == 0:
            ret.append(i)
            while a%i == 0:
                a//=i
        i+=1
    return ret

def check(a,b):
    if a == "" or b == "":
        return False
    if a == "1" or b == "1":
        return False
    y = rozklad(int(b))
    for x in rozklad(int(a)):
        if x in y:
            return False
    else:
        print(a,b)
        return True

def reku(num,a,b):
    if num ==0:
        check(a,b)
        return
    new_num = num//10
    digit = str(num%10)
    reku(new_num,digit+a,b)
    reku(new_num,a,digit+b)
def strt(num):
    a = ""
    b = ""
    reku(num,a,b)

strt(2137)
