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


def tabToLista(tab: list):
    ret = lista()
    for e in tab[::-1]:
        ret.first = Node(e, ret.first)
    return ret


# 32. Lista reprezentuje wielomian o współczynnikach całkowitych. Elementy w
# liście ułożone są według rosnących potęg. Proszę napisać funkcję
# obliczającą różnicę dwóch dowolnych wielomianów. Wielomiany reprezentowane
# są przez wyżej opisane listy. Procedura powinna zwracać wskaźnik do nowo
# utworzonej listy reprezentującej wielomian wynikowy. Listy wejściowe
# powinny pozostać niezmienione.

def odejmij(l1: lista, l2: lista):
    ret = lista(Node(0, null))
    c1, c2 = l1.first, l2.first
    last = ret.first
    while c1 != null or c2 != null:
        val = (c1.val if c1 != null else 0) + ((-1) * c2.val if c2 != null else 0)
        last.next = Node(val, null)
        last = last.next
        c1, c2 = c1.next, c2.next
    ret.first = ret.first.next
    return ret


print(odejmij(tabToLista([1, 2, 1, 2]), tabToLista([1, 1, 1, 1])))
