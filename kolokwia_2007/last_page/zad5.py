null = None


class Node:
    # val,next,idx
    def __init__(self, val=0, next=None, prev=None):
        self.next = next
        self.prev = prev
        self.val = val

    def __str__(self):
        return f"{self.val}-->"


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


def tabToLista(tab: list):
    ret = lista(Node(1))
    for e in tab[::-1]:
        ret.first = add_in_front(ret.first,e)
    return ret




# V kartkówka - WSKAŹNIKI (grupa a)
# - dana jest uporządkowana lista 2-kierunkowa, napisz procedury lub funkcje: dodawania elementu do
# listy za jakiś element i wstawiania elementu do listy na pierwsze miejsce, na ich podstawie napisz
# procedurę lub funkcję, która doda element w odpowiednie miejsce

def add_in_front(first, value):
    fi = Node(value, first, null)
    first.prev = fi
    return fi


def add_in_list(first, value):
    cp = first
    while value < cp.val and cp.next != null:
        cp = cp.next
    if cp.next == null:
        fi = Node(value, null, cp)
        cp.next = fi
    else:
        fi = Node(value, cp, cp.prev)
        cp.prev.next = fi
        cp.prev = fi
    return first


def insert(first, value):
    if first.val >= value:
        return add_in_front(first, value)
    else:
        return add_in_list(first, value)

