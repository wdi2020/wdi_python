def czy_cyfra_zlozona(num):
    if num == 0 or num == 4 or num ==1 or num == 6 or num ==8:
        return True
    return False

def func(t,MAX):
    for row in t:
        i = 0
        while i<MAX:
            copy = row[i]
            while copy>0:
                if not czy_cyfra_zlozona(copy%10):
                    break
                copy//=10
            else:
                return True
            i+=1
    return False

if __name__ == "__main__":
    #jest true bo ostatni elem 3 row
    print(func([[2,7,5,22],[23,45,65,78],[43,643,20,84],[2,34,5,3]],4))

