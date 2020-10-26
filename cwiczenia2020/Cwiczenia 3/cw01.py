a = int(input("pdoaja liczbeadfa: "))
podstawa = int(input("pdaj podsatwe: "))
#nie dawac podstawy wiekszej od 10 bo ja nie znam stringow i przyps bo nie wiem jak sie dodaje stringi:((((((
# żart jednak były stringi
new_a = ""
while a > 0:
    temp = a % podstawa
    if temp >= 10:
        #+55 bo 10+55 to A ,itd 11+55 to B
        temp = chr(temp+55)
    new_a = str(temp) + new_a
    a //= podstawa
print(new_a)
    