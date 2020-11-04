if __name__ == "__main__":
    num = int(input(">:"))
    while True:
        num += 1
        flag = False
        flag2 = False
        a1 : int = 1
        a2 : int = 1
        suma : int = 0
        b1 : int = 1
        b2 : int = 1

        while True:
            suma += a1
            if num- suma == 0 :
                break
            if flag: break
            if suma > num:
                suma_copy = suma
                while True:
                    if suma - b1 == num:
                        flag2 = True
                        break
                    if suma - b1 < num:
                        flag = True
                        break
                    suma -= b1
                    new_number_b = b1 + b2
                    b1 = b2
                    b2 = new_number_b
            if flag2: break
            new_number = a1 + a2
            a1 = a2
            a2 = new_number
        if flag: break
    print(num)
            