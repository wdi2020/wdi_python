#cw 10
def cw10():
    num = int(input('>: '))
    a1 = 2
    a2 = (3*a1)+1
    while a1 <= num:
        mnoznik = 1
        while a1*mnoznik < num:
            mnoznik += 1
        
        if a1*mnoznik == num: return True
        a1,a2 = a2,(3*a1)+1
    return False

if __name__ == "__main__":
    print(cw10())