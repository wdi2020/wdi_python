from random import randint
def cw1():
    a = 5
    b = 8
    print(a,b)
    #classic
    temp = a
    a = b
    b = temp
    print("po classic",a,b)
    #python way
    a,b = b,a
    print("po python way", a , b)

def rand_dict(n):
    return {randint(0,20):randint(0,20) for _ in range(n)}

def reverse_dict(dictionary : dict):
    return {val:key for key,val in dictionary.items()}

def cw2():
    di = rand_dict(20)
    print(di)
    print(len(di))
    print(reverse_dict(di))

def cw3():
    k = 2
    given_string = "ma kota ala ala ala kota kota"
    given_string = given_string.split(" ")
    counted_S = {}
    for letter in given_string:
        counted_S[letter] = counted_S.get(letter, 0) + 1
    print(sorted(counted_S, 
                key=lambda x: counted_S[x],
                reverse=True)[0 : k])

def cw4():
    color = "209 209 209"
    dictionary : dict = {}
    with open("colors.txt","r") as file:
        dictionary = {item.split(':')[0] : item.split(':')[1] for item in file.readlines()}
    for key,value in dictionary.items():
        if color in value:
            print(key)
            break

def cw5():
    with open("products.txt","r") as file:
        products_to_buy = file.readline().replace("\n","").split(", ")
        file.readline()
        lines = file.readlines()
        for line in lines:
            for item in line.replace("\n","").split(", "):
                prod = products_to_buy.copy()
                if item in prod:
                    products_to_buy.remove(item)
        if len(products_to_buy) == 0:
            print('ok')
        else:
            print("not ok")
            print(products_to_buy)

import json
def cw7():
    json_set = list()
    header_dict = []
    with open("comma.csv", "r") as file:
        header_dict = [item for item in file.readline().replace("\n","").split(',')]
        for line in file.readlines():
            i = 0
            line = line.replace("\n","").split(",")
            dictionary = {}
            for item in line:
                dictionary[header_dict[i]] = item
                i += 1
            json_set.append(dictionary)
    with open("file.json", "w+") as file:
        json.dump(json_set, file)


if __name__ == "__main__":
    cw7()