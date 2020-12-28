# 3.Mamy cykliczną listę zawierającą liczby całkowite. Każda pierwsza cyfra kolejnej liczby jest równa
# ostatniej cyfrze poprzedniej liczby.
# np. 123 - 324 - 435 - 578 -> łańcuch się zapętla
# Napisz funkcję wstawiającą liczbę do listy. Liczba ma zastąpić dwie już istniejące elementy cyklu.
# dla przykładu tutaj, za (324 - 435) można wstawić 35
# Funkcja powinna zwrócić wartość logiczną w zależności od tego czy próba wstawiania zakończyła się
# sukcesem.
null = None


class lista:
    def __init__(self, first=null):
        self.first = first

    def __str__(self):
        cp = self.first
        cp2 = self.first.next
        if cp == null:
            return "List is empty!"
        ret = str(cp)
        while cp != cp2:
            ret = ret + str(cp2)
            cp2 = cp2.next
        return ret


class Node:
    # val,next,idx
    def __init__(self, val=0, next=None):
        self.next = next
        self.val = val

    def __str__(self):
        return f"{self.val}-->"


def tabToLista(tab: list):
    ret = lista()
    for e in tab[::-1]:
        ret.first = Node(e, ret.first)
    return ret


def insert_if_possible(first, val):
    cp = val
    fi = 0
    while cp != 0:
        fi =cp%10
        cp //= 10
    la = val % 10
    print(fi,la)
    cp, cp2 = first, first.next
    while cp != cp2:
        if cp2.val % 10 == fi and cp2.next.next.val % 10 == la:
            temp = cp2.next.next.next
            cp2.next = Node(val, temp)
            print(lista(cp2))
            return True
        cp2 = cp2.next
    return False


tab = [12, 23, 34, 45, 56, 67, 78, 81]
listaa = tabToLista(tab)
cp = listaa.first
while cp.next != null:
    cp = cp.next
cp.next = listaa.first
print(listaa)
print(insert_if_possible(listaa.first, 57))
