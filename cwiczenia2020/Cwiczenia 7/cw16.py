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


# 16. Proszę napisać funkcję, która otrzymując jako parametr wskazujący na
# początek listy jednokierunkowej, przenosi na początek listy te z nich,
# które mają parzystą ilość piątek w zapisie ósemkowym.

def ile_5(num):
    ilosc = 0
    while num != 0:
        if num % 8 == 5:
            ilosc += 1
        num //= 8
    return ilosc


def move(first, cp, cp2):
    cp.next = cp2.next
    cp2.next = first
    return cp2


def check(first):
    if first == null:
        return null
    if first.next == null:
        return first
    cp, cp2 = first, first.next
    while cp2 != null:
        if ile_5(cp2.val) % 2 == 0:
            first = move(first, cp, cp2)
            cp2 = cp.next
        else:
            cp, cp2 = cp2, cp2.next
    return first


first = Node(1)
for i in range(10):
    a = Node(5, first)
    first = a
wypisz(first)
wypisz(check(first))
