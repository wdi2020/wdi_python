#2. Wyrazy budowane są z liter a..z. Dwa wyrazy „ważą” tyle samo jeżeli: mają tę samą liczbę samogłosek 
#oraz sumy kodów ascii liter z których są zbudowane są identyczne, 
#na przykład „ula” -> 117 108 97 oraz „exe” 101 120 101. 
#Proszę napisać funkcję bool wyraz( string s1, string s2), 
#która sprawdza czy jest możliwe zbudowanie wyrazu z podzbioru liter zawartych w s2 ważącego tyle co wyraz s1. 
#Dodatkowo funkcja powinna wypisać znaleziony wyraz.

def check(s1,s2):
    samogloski = ('a','e','i','y','u','o')
    sum1 = 0
    il_sam = 0
    for letter in s1:
        sum1 += ord(letter)
        if letter in samogloski:
            il_sam+=1
    for letter in s2:
        sum1 -= ord(letter)
        if letter in samogloski:
            il_sam-=1
    if sum1 == il_sam == 0:
        return True
    return False

def reku(s1,s2,s,idx):
    if idx == len(s2):
        if check(s1,s):
            return s
        return ""
    a = reku(s1,s2,s,idx+1)
    if a != "":
        return a
    return reku(s1,s2,s+s2[idx],idx+1)

def strt(s1,s2):
    return reku(s1,s2,"",0)

print(strt("ula1","exekdafhd1akfja"))