a = int(input("pdoaja liczbeadfa: "))
podstawa = int(input("pdaj podsatwe: "))
new_a = ""
while a > 0:
    temp = a % podstawa
    if temp >= 10:
        #+55 bo 10+55 to A ,itd 11+55 to B
        temp = chr(temp+55)
    new_a = str(temp) + new_a
    a //= podstawa
print(new_a)
    