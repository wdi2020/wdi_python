def check():
    with open("dane.txt","r") as file:
        lines = file.readlines()
    pozycje = []
    for line in lines:
        po = line.split(" ")
        pozycje.append((int(po[0]),int(po[1])))
    kolumny = [0 for _ in range(100)]
    wiersze = [0 for _ in range(100)]
    l_diag = [0 for _ in range(201)]
    r_diag = [0 for _ in range(201)]

    for elem in pozycje:
        if kolumny[elem[1]] == 1:
            return True
        kolumny[elem[1]] = 1
        if wiersze[elem[0]] == 1:
            return True
        wiersze[elem[0]] = 1
        if l_diag[100+elem[0]-elem[1]] == 1:
            return True
        l_diag[100+elem[0]-elem[1]] = 1
        if r_diag[100+elem[1]-elem[0]] == 1:
            return True
        r_diag[100+elem[1]-elem[0]] = 1
    return False

print(check())
