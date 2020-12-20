null = None


class lista:
    def __init__(self, first=null):
        self.first = first

    def __str__(self):
        cp = self.first
        if cp == null:
            return "List is empty!"
        ret = ""
        while cp != None:
            ret = ret + str(cp)
            cp = cp.next
        return ret

    def is_empty(self):
        return self.first == null


class Node:
    # val,next,idx
    def __init__(self, val=0, next=None):
        self.next = next
        self.val = val

    def __str__(self):
        return f"{self.val}-->"

    def __lt__(self, other):
        return self.val < other.val

    def __gt__(self, other):
        return self.val > other.val

    def __le__(self, other):
        return self.val <= other.val


# 31. Proszę napisać funkcję, która rozdziela listę na dwie listy. Pierwsza
# powinna zawierać klucze parzyste dodatnie, drugi klucze nieparzyste ujemne,
# pozostałe elementy należy usunąć z pamięci. Do funkcji należy przekazać
# wskaźniki na listę z danymi oraz wskaźniki na listy wynikowe. Funkcja
# powinna zwrócić liczbę usuniętych elementów.

def rozdziel(lis: lista, parzysta_lista: lista, np_ujemna_lista: lista):
    if lis.is_empty():
        return False
    cp = lis.first
    while cp != null:
        if cp.val % 2 == 0 and cp.val >= 0:
            parzysta_lista.first = Node(cp.val, parzysta_lista.first)
            lis.first = lis.first.next
            del cp
            cp = lis.first
            continue
        if cp.val < 0 and (cp.val * (-1)) % 2 == 1:
            np_ujemna_lista.first = Node(cp.val, np_ujemna_lista.first)
            lis.first = lis.first.next
            del cp
            cp = lis.first
            continue
        else:
            lis.first = lis.first.next
            del cp
            cp = lis.first
            continue
    return True


def tabToLista(tab: list):
    ret = lista()
    for e in tab[::-1]:
        ret.first = Node(e, ret.first)
    return ret


l1 = tabToLista([1, 3, 5, 7, 9, 13, 21, -1, -3, 0, 34, -7, -37])
parzysta = lista()
np_ = lista()
rozdziel(l1, parzysta, np_)
print(parzysta)
print(l1)
print(np_)
