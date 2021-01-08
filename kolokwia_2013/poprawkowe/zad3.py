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
def tabToLista(tab:list):
    ret = lista()
    for e in tab[::-1]:
        ret.first = Node(e,ret.first)
    return ret


#3. Mamy 2 uporządkowane listy jednokierunkowe. Napisz funkcję, która zwróci wskaźnik na różnicę
#symetryczną z obu list (czyli taki XOR).
#rosnąca lista

def xor(first,second):
    nowa = Node(0,null)
    nowa_last = nowa
    cp = first
    cp2 = second
    while cp != null and cp2 != null:
        if cp.val < cp2.val:
            nowa_last.next = Node(cp.val,null)
            nowa_last = nowa_last.next
            cp = cp.next
        elif cp2.val < cp.val:
            nowa_last.next = Node(cp2.val,null)
            nowa_last = nowa_last.next
            cp2 = cp2.next
        else:
            cp,cp2 = cp.next,cp2.next
    while cp!= null:
        nowa_last.next = Node(cp.val, null)
        nowa_last = nowa_last.next
        cp = cp.next
    while cp2!= null:
        nowa_last.next = Node(cp2.val, null)
        nowa_last = nowa_last.next
        cp2 = cp2.next
    return nowa.next

tab = [0, 1, 2, 3, 4, 5, 6, 7, 8, 12, 13]
tab2 = [0,1,2,4,5,6,7,8,89,123]
print(tabToLista(tab))
print(tabToLista(tab2))
print(lista(xor(tabToLista(tab).first,tabToLista(tab2).first)))

