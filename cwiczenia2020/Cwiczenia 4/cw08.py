def cw08(t1,MAX):
    #to maxtmalna dl ciagu
    c_amx = 0
    i = 0
    #max-3 bo dalsze indexy w kolumnach spowoduja niemozliwosci uzyskania ciagu o dl 3
    while i <= MAX-3:
        #count to dl ciagu 
        count = 0
        #copy to index na columnie, row to index na wieszu
        copy  = i+1
        row = 1
        #startuje od a1 w ciagu an = a1 * q^(n-1)
        a1 = t1[0][i]
        #randomowe q ale nie dawac 0 bo przypal
        q = 12
        #column index do maxa bo inaczej za tabem bd 
        while copy <MAX:
            # jak q == 0 to jest dziwnie i wild
            if q == 0:
                break
            # to jak sie spelni poprzedni * q == terazniejszy, to ciag
            if a1 * q == t1[row][copy]:
                #tu wsm to a1 sie zmienia bo to jest a z indexem n-1 w ciagu an = a *q
                a1 = a1*q
                count +=1
            else:
                # jak a1 == 0  to q by bylo z dzieleniem przez 0
                if a1 == 0:
                    break
                #a1 sie zmienia to takie cos to q bd git dla nastepnych
                q = t1[row][copy] / a1
                #count 2 bo a1 to pierwszy wyraz a t1[row][column] to drugi
                count = 2
            #koniec petli prawie tylkko dodac do row i copy(column)
            row+=1
            copy+=1
        #...
        if count > c_amx :
            c_amx = count
        i+=1

    if c_amx >=3:
        return True,c_amx
    return False

from random import randint
if __name__ == "__main__":
    print(cw08([[randint(1,100) for _ in range(100)] for _ in range(100)],100))
