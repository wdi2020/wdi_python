#cw 2
if __name__ == "__main__":
    a = 6
    b = 7
    n  = 100
    print(a//b, end="")
    a = a%b
    print(".",end="")
    while n >0:
        if a < b:
            a *= 10
            print(a//b, end="")
            a = a%b
        else:
            print(a//b,end="")
            a = a%b
        n-= 1