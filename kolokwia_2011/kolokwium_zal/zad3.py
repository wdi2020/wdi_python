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


# 3. Dane są dwa niepuste łańcuchy odsyłaczowe [jednokierunkowe] przechowujące liczby
# naturalne. W pierwszym liczby są uporządkowane rosnąco, a w drugim malejąco. Proszę
# napisać odpowiednie definicje typów oraz funkcję scalającą takie dwa łańcuchy w jeden
# zawierający posortowane rosnąco elementy. Funkcja powinna zwrócić wskaźnik do nowego
# łańcucha.

def scal(first, second):
    # first jest rosnaco
    # a second malejaco
    if second == null:
        return first
    if first == null:
        first = second
        second = second.next
    while second != null:
        cp = first
        v = second
        if cp.val >= v.val:
            second = second.next
            v.next = cp
            first = v
            continue
        while cp.next != null and cp.next.val < v.val:
            cp = cp.next
        second = second.next
        v.next = cp.next
        cp.next = v
    return first


tab = [i for i in range(10)]
tab2 = [10 - i for i in range(10)]
print(tabToLista(tab))
print(tabToLista(tab2))
print(lista(scal(tabToLista(tab).first, tabToLista(tab2).first)))
