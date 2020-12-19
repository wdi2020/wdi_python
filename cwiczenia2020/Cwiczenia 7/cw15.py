null = None

class Node:
    def __init__(self, value=null, next=null):
        self.val = value
        self.next = next

    def __str__(self):
        return f"{self.val}-->"


def wypisz(first):
    if first == null:
        print("List is empty!")
    while first != null:
        print(first, end='')
        first = first.next
    print()


# !15. Proszę napisać funkcję, która otrzymując jako parametr wskazujący na
# !początek listy jednokierunkowej, usuwa z niej wszystkie elementy, w których
# !wartość klucza w zapisie trójkowym ma większą ilość jedynek niż dwójek.
def delete(cp, cp2):
    cp.next = cp2.next
    del cp2
    return cp


def check_3(num):
    i_1 = 0
    i_2 = 0
    while num != 0:
        a = num % 3
        if a == 1:
            i_1 += 1
        if a == 2:
            i_2 += 1
        num //= 3
    return i_1 > i_2


def check(first):
    while first != null and check_3(first.val):
        first = first.next
    if first == null:
        return null
    cp, cp2 = first, first.next
    while cp2 != null:
        if check_3(cp2.val):
            delete(cp, cp2)
        cp, cp2 = cp2, cp2.next
    return first


first = null
for i in range(20):
    a = Node(16, first)
    first = a
wypisz(first)
wypisz(check(first))
