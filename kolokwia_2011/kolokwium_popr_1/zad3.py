# 1. Mamy tablicę [1..max,1..max] of integer. Wyzeruj w niej wszystkie liczby które nie mają w tablicy innej
# liczby, która powstałaby poprzez przestawienie jej cyfr. (uważając na 1000 i 0100 - nie dziala).
# todo zadanie 1
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


tab = [i for i in range(10)]
tab2 = [i + 2 for i in range(10)]
print(tabToLista(tab))
print(tabToLista(tab2))


# 3. Mamy 2 uporządkowane listy jednokierunkowe. Napisz funkcję, która zwróci wskaźnik na różnicę
# symetryczną z obu list (czyli taki XOR).

# zalozmy ze uporzdkowane rosnaco

def xor(first, second):
    nowa = null
    nowa_end = null
    cp = first
    cp2 = second
    while cp != null and cp2 != null:
        if cp.val < cp2.val:
            if nowa != null:
                nowa_end.next = Node(cp.val, null)
                nowa_end = nowa_end.next
            else:
                nowa = Node(cp.val, null)
                nowa_end = nowa
            cp = cp.next
        elif cp2.val < cp.val:
            if nowa != null:
                nowa_end.next = Node(cp2.val, null)
                nowa_end = nowa_end.next
            else:
                nowa = Node(cp2.val, null)
                nowa_end = nowa
            cp2 = cp2.next
        else:
            cp, cp2 = cp.next, cp2.next
    while cp != null:
        nowa_end.next = Node(cp.val, null)
        nowa_end = nowa_end.next
        cp = cp.next
    while cp2 != null:
        nowa_end.next = Node(cp2.val, null)
        nowa_end = nowa_end.next
        cp2 = cp2.next
    return nowa


print(lista(xor(tabToLista(tab).first, tabToLista(tab2).first)))
