# Zadanie 16. Wyrazy budowane są z liter a..z. Dwa wyrazy ”ważą” tyle samo jeżeli: 
# mają tę samą liczbę samogłosek oraz sumy kodów ascii liter z których są zbudowane są identyczne, 
# na przykład 00ula00 → 117, 108, 97 oraz 00exe00 → 101, 120, 101. 
# Proszę napisać funkcję wyraz(s1,s2), 
# która sprawdza czy jest możliwe zbudowanie wyrazu z podzbioru liter zawartych w s2 ważącego tyle co wyraz s1. 
# Dodatkowo funkcja powinna wypisać znaleziony wyraz.

def ilosc_samoglosek(s):
    samogloski = ["a","e","i","o","u","y"]
    count = 0
    for i in s:
        if i in samogloski:
            count+=1
    return count
def czy_ascii(s1,s2):
    sum1 = 0
    for i in s1:
        sum1 += ord(i)
    sum2 = 0
    for i in s2:
        sum2+= ord(i)
    return sum1 == sum2
def reku(s,index,curr_s,szukany):
    if czy_ascii(szukany,curr_s) and ilosc_samoglosek(szukany) == ilosc_samoglosek(curr_s):
        return True
    if index == len(s):
        return False
    if reku(s,index+1,curr_s,szukany):
        return True
    if reku(s,index+1,curr_s+s[index],szukany):
        return True
    return False
def func(s1,s2):
    return reku(s2,0,"",s1)

print(func("00ula00","01exe01")) #false