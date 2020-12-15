#2. Zastosowanie listy odsyłaczowej do implementacji
#tablicy rzadkiej. Proszę napisać trzy funkcje:
#– inicjalizującą tablicę,
#– zwracającą wartość elementu o indeksie n,
#– podstawiającą wartość value pod indeks n.
class Node:
    #val,next,idx
    def __init__(self,val=0,next=None,idx=-1):
        self.next = next
        self.val = val
        self.idx = idx
    def __str__(self):
        return f"{self.idx},{self.val}"

def init():
    print("brrr..... init ")
    return Node()

def insert(first,idx,val):
    def is_in_list(first,idx):
        cp = first
        while cp != None:
            if cp.idx > idx:
                return None
            if cp.idx == idx:
                return cp
            cp = cp.next
        return None

    a =  is_in_list(first,idx)
    if a != None:
        a.val = val
        return
    bef=first
    cp = bef.next
    while cp != None and cp.idx<idx:
        bef,cp = cp,cp.next
    if cp != None:
        new_node = Node()
        new_node.next = cp
        new_node.val = val
        new_node.idx = idx
        bef.next = new_node
    else:
        new_node = Node()
        new_node.val = val
        new_node.idx = idx
        new_node.next = None
        bef.next = new_node
    return

def get(first,idx):
    if first == None:
        return None
    def is_in_list(first,idx):
        cp = first
        while cp != None:
            if cp.idx > idx:
                return None
            if cp.idx == idx:
                return cp
            cp = cp.next
        return None
    return is_in_list(first,idx)

def wypisz(first):
    bef = first.next
    while bef != None:
        print(bef)
        bef = bef.next

a = init()
for i in range(10):
    insert(a,i,i+1)
for i in range(10):
    print(get(a,i))