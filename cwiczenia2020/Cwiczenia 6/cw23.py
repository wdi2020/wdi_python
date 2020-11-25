#Zadanie 23. Dana jest tablica T[N] zawierająca oporności N rezystorów wyrażonych całkowitą liczbą
#kΩ. Proszę napisać funkcję, która sprawdza czy jest możliwe uzyskanie wypadkowej rezystancji R (równej
#całkowitej liczbie kΩ) łącząc dowolnie 3 wybrane rezystory
def can_be(target,indexes:str):
    if len(indexes) <3:
        return False
    x1,x2,x3 = int(indexes[0]),int(indexes[1]),int(indexes[2])
    if x1+x2+x3 == target:
        return True
    elif (x1*x2*x3)/((x1*x2)+(x2*x3)+(x1*x3)) == target:
        return True
    elif (x1*x2)/(x1+x2) + x3 == target:
        return True
    elif (x1*x3)/(x1+x3) + x2 == target:
        return True
    elif (x2*x3)/(x2+x3) + x1 == target:
        return True
    return False
def reku(tab,index,indexes,idx_pom,target):
    if idx_pom == 3:
        if can_be(target,indexes):
            return True
        return False
    if index == len(tab):
        return False
    if reku(tab,index+1,indexes,idx_pom,target):
        return True
    indexes[idx_pom] = tab[index]
    idx_pom+=1
    if reku(tab,index+1,indexes,idx_pom,target):
        return True
    return False

def func(tab,target):
    return reku(tab,0,[0 for _ in range(3)],0,target)

print(func([10,20,234,23423,12323,557,657,34,21,434,70,5652332,45,5,324,4,3,1],70+(20/3))) #True 10,20,70
