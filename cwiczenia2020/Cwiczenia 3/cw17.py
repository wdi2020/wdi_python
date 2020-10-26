def czy_pierwsza(num):
    if num <=1:
        return False
    if num == 2 or num ==3 :
        return True
    if num %2==0 or num%3 == 0:
        return False
    i = 6
    while i*i <= num:
        if num%i-1 ==0 or num %i+1 == 0:
            return False
        i+= 6
    return True

def rekurencja(tab1,tab2,lengh,suma,tryb,index):
#tryb 0-z pierwszej
#1 z drugiej
#2 z obu
    if tryb == 0:
        suma += tab1[index]
    elif tryb ==1:
        suma += tab2[index]
    else:
        suma += tab1[index]
        suma += tab2[index]
    index +=1
    if index < lengh:
        rekurencja(tab1,tab2,lengh,suma,0,index)
        rekurencja(tab1,tab2,lengh,suma,1,index)
        rekurencja(tab1,tab2,lengh,suma,2,index)
    else:
        if czy_pierwsza(suma):
            print(suma)
def sumy_pierwsze(tab1,tab2):
    lengh = len(tab1)
    index = 0
    rekurencja(tab1,tab2,lengh,0,0,index)
    rekurencja(tab1,tab2,lengh,0,1,index)
    rekurencja(tab1,tab2,lengh,0,2,index)

if __name__ == "__main__":
    sumy_pierwsze([1,3,2,4],[9,7,4,8])