#1. Proszę napisać program, który wczytuje wprowadzany z klawiatury ciąg liczb naturalnych
#zakończonych zerem stanowiącym wyłącznie znacznik końca danych.
#Program powinien wypisać te elementy ciągu które są równe średniej arytmetycznej z 4 najbliższych
#sąsiadów. Na przykład dla ciągu: 2,3,2,7,1,2,4,8,5,2,2,4,3,9,5,4,0 powinny zostać wypisane
#podkreślone liczby. Można założyć, że w ciągu znajduje się co najmniej 5 elementów.

a = input()
tablica = a.split(",")
for i in range(len(tablica)):
    tablica[i] = int(tablica[i].strip())
tablica.pop(len(tablica)-1)
for i in range(len(tablica)):
    sr = 0
    if i < 2:
        for j in range(5):
            sr += tablica[j]
    elif i > (len(tablica)-3):
        for j in range(5):
            sr += tablica[len(tablica)-1-j]
    else:
        sr += tablica[i-2]
        sr += tablica[i-1]
        sr += tablica[i]
        sr += tablica[i+2]
        sr += tablica[i+1]
    if sr/5 == tablica[i]:
        print(tablica[i])


