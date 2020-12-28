def czy_pierwsza(num):
    if num <=1:
        return False
    if num ==2 or num ==3:
        return True
    if num %2==0 or num%3==0:
        return False
    i = 6
    while (i-1)**2<=num:
        if num %(i-1) == 0:
            return False
        if num%(i+1) == 0:
            return False
        i+=6
    return True

li = int(input(">"))

for i in range(3,10):
    copy = li
    while copy !=0:
        cyf = copy%i
        copy//=i
        if not czy_pierwsza(cyf):
            break
    else:
        print("wszystkie cyfry sa pierwsze")
        break
