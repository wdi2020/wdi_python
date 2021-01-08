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

#tu sie zaczyna
def make(n):
    if n == -1:
        return null
    first = Node(n)
    first.next = make(n - 1)
    return first


print(lista(make(10)))