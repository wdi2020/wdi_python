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

def tabToLista(tab:list):
    ret = lista()
    for e in tab[::-1]:
        ret.first = Node(e,ret.first)
    return ret

tab = [i for i in range(10)]
print(tabToLista(tab))


def reverse(first):
    def reku(first):
        if first.next ==null:
            return first,first
        cp,last = reku(first.next)
        first.next = null
        last.next = first
        return cp,last.next

    cp,last = reku(first)
    return cp


print(lista(reverse(tabToLista(tab).first)))