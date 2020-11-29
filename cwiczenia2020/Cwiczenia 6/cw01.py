def czy_pierwsza(num):
    if num <10:
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

def rekur(num,curr_index,dl,curr_num):
    if curr_index+1 > dl:
        return
    rekur(num,curr_index+1,dl,curr_num)
    num2 = 0
    if curr_num != 0:
        num2 = (num%(10**(curr_index+1))//(10**curr_index))*(10**(len(str(curr_num))))
    else:
        num2 = (num%(10**(curr_index+1))//(10**curr_index))
    num1 = curr_num + num2
    if czy_pierwsza(num1):
        print("liczba pierwsza -> ",num1)
    rekur(num,curr_index+1,dl,num1)

def pierwsze_liczby(num):
    rekur(num,0,len(str(num)),0)


pierwsze_liczby(127127)