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


# 3. Dany jest typ:
# type
# pnode=^node;
# node=record
# klucz:integer;
# next:pnode;
# end;
# Proszę napisać procedurę rozdzielającą łańcuch na 2 łańcuchy według klucza, w taki sposób,
# że w pierwszym łańcuchu znajdą się liczby, które są wielokrotnością kwadratu
# liczby pierwszej, a w drugim pozostałe.


def check(num):
    # sito bylo by dobrym pomyslem
    # ale jestem za leniwy siema
    if num <= 1:
        return False
    i = 2
    while i * i <= num:
        if num % (i * i) == 0:
            return True
        # to +1 jest tragiczne
        i += 1
    return False


def rozdziel(first):
    kwadraty = null
    pozostale = null
    while first != null:
        cp = first
        first = first.next
        if check(cp.val):
            cp.next = kwadraty
            kwadraty = cp
        else:
            cp.next = pozostale
            pozostale = cp
    print(lista(kwadraty))
    print(lista(pozostale))


tab = [i for i in range(26)]
first = tabToLista(tab)
print(first)
rozdziel(first.first)
