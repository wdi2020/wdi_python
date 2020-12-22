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


# 33. Napis s1 poprzedza napis s2 jeżeli ostatnia litera s1 jest „mniejsza”
# od pierwszej litery s2. Według tej zasady rozmieszczono napisy w liście
# cyklicznej, na przykład:
# ┌─bartek──leszek──marek──ola──zosia─┐
# └───────────────────────────────────┘
# Proszę napisać stosowne definicje typów oraz funkcję wstawiającą do listy
# napis z zachowaniem zasady poprzedzania. Do funkcji należy przekazać
# wskaźnik do listy oraz wstawiany napis, funkcja powinna zwrócić wartość
# logiczną wskazującą, czy udało się wstawić napis do listy. Po wstawieniu
# elementu wskaźnik do listy powinien wskazywać na nowo wstawiony element.

# sprawdza czy cp jest mniejszy od cp2
def mniejszy(cp, cp2):
    if ord(cp.val[-1]) < ord(cp2.val[0]):
        return True
    return False


def insert(l: lista, val):
    fir = l.first
    cp_val = Node(val, null)
    cp, cp2 = l.first, l.first.next
    while fir != cp2:
        if mniejszy(cp_val, cp2):
            cp.next = cp_val
            cp_val.next = cp2
            l.first = cp_val
            return
        cp, cp2 = cp2, cp2.next
    cp.next = cp_val
    cp_val.next = cp2
    l.first = cp_val
    return


last = Node("zosia")
first = Node("bartek", Node("leszek", Node("marek", Node("ola", last))))
last.next = first
listaa = lista(first)
print(listaa)
# bartek──leszek──marek──ola──zosia
insert(listaa, "ala_ma_kotd")
print(listaa)
