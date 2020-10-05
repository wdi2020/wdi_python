#NA BIT PYTHON Z 27.09
def main():
    tablica = [[None for _ in range(3)] for _ in range(3)]
    x = 'x'
    o = 'o'
    gra_x : bool = False
    koniec : bool = False
    while True:
        
        for i in range(3):
            print("---------")
            for j in range(3):
                print("|",end="")
                if tablica[i][j] == None:
                    print(" ",end="")
                else:
                    print(tablica[i][j],end="")
                print("|",end="")
                if j == 2:
                    print()
        gra_x = not gra_x
        for i in range(3):
            if tablica[i][0] == tablica[i][1] == tablica[i][2] != None:
                if tablica[i][0] == 'x':
                    print("1 gracz wygrywa")
                else:
                    print("2 gracz wygrywa")
                koniec = True
                break
        for i in range(3):
            if tablica[0][i] == tablica[1][i] == tablica[2][i] != None:
                if tablica[0][i] == 'x':
                    print("1 gracz wygrywa")
                else:
                    print("2 gracz wygrywa")
                koniec = True
                break
        if tablica[0][0] == tablica[1][1] == tablica[2][2] != None:
            if tablica[0][0] == 'x':
                print("1 gracz wygrywa")
            else:
                print("2 gracz wygrywa")
            koniec = True
            break
        if tablica[0][2] == tablica[1][1] == tablica[2][0] != None:
            if tablica[0][0] == 'x':
                print("1 gracz wygrywa")
            else:
                print("2 gracz wygrywa")
            koniec = True
            break
        ans_list = []
        for i in range(3):
            ans_list.extend(list(filter(lambda x : x == None, tablica[i])))
        if ans_list == []:
            print("remis")
            koniec = True
            break
        if koniec == True:
            break
        ruch = int(input(f"Witam podaj dla cyfre do ruchu {x if gra_x else o} :"))

        for i in range(3):
            for j in range(3):
                curr_index = i*3 + j +1
                if curr_index == ruch:
                    if tablica[i][j] != None:
                        gra_x = not gra_x
                        print("Zajete")
                        break
                    else:
                        tablica[i][j] = x if gra_x else o 



if __name__ == "__main__":
    main()