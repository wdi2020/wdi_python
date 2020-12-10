#1. Proszę napisać program, który wczytuje wprowadzany z klawiatury ciąg liczb naturalnych
#zakończonych zerem stanowiącym wyłącznie znacznik końca danych.
#Program powinien wypisać 10 co do wielkości wartość, jaka wystąpiła w ciągu.
#Na przykład dla ciągu: 1,2,3,2,3,4,5,6,7,8,9,9,11,12,13,0 powinna zostać wypisana liczba 3.
#Można założyć, że w ciągu znajduje się wystarczająca liczba elementów
def insert(idx,num,tab):
    if tab[idx] == 0:
        tab[idx] = num
        return
    tab[idx],buf = num,tab[idx]
    for i in range(idx+1,len(tab)):
        buf,tab[i] = tab[i],buf
    print(tab)

def strt():
    tablicka = [0 for _ in range(10)]
    idx =0
    a = input()
    while a != "0":
        num = int(a)
        curr_idx = 0
        for i in range(idx):
            if num > tablicka[i]:
                break
            curr_idx +=1
        if curr_idx >= 0 and curr_idx < len(tablicka):
            insert(curr_idx,num,tablicka)
            idx+=1
        a = input()
    print(tablicka[9])

strt()
