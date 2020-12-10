#2. Dane są dwie liczby naturalne z których budujemy trzecią liczbę. 
#W budowanej liczbie muszą wystąpić wszystkie cyfry występujące w liczbach wejściowych. Wzajemna kolejność cyfr każdej z 
#liczb wejściowych musi być zachowana. Na przykład mając liczby 123 i 75 możemy zbudować liczby 12375,17523, 75123, 17253, itd. 
#Proszę napisać funkcję która wyznaczy ile liczb pierwszych można zbudować z dwóch zadanych liczb.

def is_prime(num):
    if num <= 1:
        return False
    if num ==2 or num ==3:
        return True
    if num%2==0 or num%3==0:
        return False
    i =5
    while i**2 <= num:
        if num%i==0 or num%(i+2)==0:
            return False
        i+=6
    return True

def reku(num1,num2,numm=0):
    if num1 == 0 and num2 == 0:
        if is_prime(numm):
            return 1
        return 0
    a = 0
    if num1 != 0:
        a+=reku(num1//10,num2,(numm*10)+(num1%10))
    if num2 != 0:
        a+=reku(num1,num2//10,(numm*10)+(num2%10))
    return a

print(reku(1,3))