# (re,im)
# liczba zespo
def dodawanie_zespo(l1,l2):
    return (l1[0]+l2[2],l1[1]+l2[1])
def odejmowanie_zespo(l1,l2):
    return (l1[0]-l2[0],l1[1]-l2[1])
def mnozenie_zespo(l1,l2):
    return (l1[0]*l2[0] - l1[1]*l2[1], (l1[0]*l2[1] + l2[0]*l1[1]))
def dzielenie_zespo(l1,l2):
    return (((l1[0]*l2[0]) + (l1[1]*l2[1]))/((l2[0]**2) + (l2[1] ** 2)),((l2[0]*l1[1])-(l2[1]*l1[0]))/((l2[0]**2) + (l2[1] ** 2)))
def wypisywanie(l1):
    print(f"({l1[0]} + {l1[1]}i)")
def wczytywanie():
    return (int(input("RE:")),int(input("IM:")))