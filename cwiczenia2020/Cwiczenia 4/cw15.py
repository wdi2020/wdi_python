def czy_pierwsza(num):
    #to tylko cyfry pierwsze nie liczby
    if num == 2 or num == 3 or num ==5 or num ==7:
        return True
    return False

def funcn(t,MAX):
    for row in t:
        i = 0
        jest = False
        while i<MAX:
            copy = row[i]
            j = False
            while copy>0:
                if czy_pierwsza(copy%10):
                    j = True
                copy//=10
            if not j:
                break
            i+=1
        else:
            return True
    return False


if __name__ == "__main__":
    print(funcn([[23,26,35,71],[21,123,45,8],[4,4,4,4],[6,6,8,3]],4))

