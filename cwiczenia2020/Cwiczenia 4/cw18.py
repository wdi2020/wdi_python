# nie dzilaaaa
def func(t,MAX):
    max_podciag = 10
    max_sum = t[0][0]
    il_pion,il_poziom = 0,0
    i = 0
    while i<MAX:
        il_pion,il_poziom = 0,0
        suma_poziom,suma_pion = 0,0
        j = 0
        while j<MAX:
            #poziom
            if il_poziom == max_podciag:
                suma_poziom -= t[i][j-10]
                il_poziom-=1
            if il_poziom < max_podciag: 
                suma_poziom += t[i][j]
                il_poziom+=1
            if suma_poziom>max_sum:
                max_sum = suma_poziom
            #pion
            if il_pion == max_podciag:
                suma_pion -= t[j-10][i]
                il_pion-=1
            if il_pion < max_podciag:
                suma_pion += t[j][i]
                il_pion+=1
            if suma_pion > max_sum:
                max_sum = suma_pion

            #usuwanie
            copy_poziom = suma_poziom
            copy_pion = suma_pion
            k = 0
            while k<j:
                #poziom
                copy_poziom -= t[i][k]
                if copy_poziom > max_sum:
                    max_sum = copy_poziom 
                #pion
                copy_pion -=t[k][i]
                if copy_pion >max_sum:
                    max_sum = copy_pion
                k+=1
            j+=1
        i+=1
    return max_sum

from random import randint
if __name__ == "__main__":
    #nie dziala dla <0 ale chuj w to
    MAX = 100
    print(func([[-100 for _ in range(MAX)] for _ in range(MAX)],MAX))