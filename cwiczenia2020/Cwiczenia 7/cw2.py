#2. Zastosowanie listy odsyłaczowej do implementacji
# tablicy rzadkiej. Proszę napisać trzy funkcje:
# – inicjalizującą tablicę,
# – zwracającą wartość elementu o indeksie n,
# – podstawiającą wartość value pod indeks n.
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

    a = is_in_list(first,idx)
    if a != None:
        a.val = val
        return
    bef=first
    cp = bef.next
    while cp != None and cp.idx<idx:
        bef,cp = cp,cp.next
    
    new_node = Node()
    new_node.next = cp
    new_node.val = val
    new_node.idx = idx
    bef.next = new_node
    return

def get(first,idx):
    def is_in_list(first,idx):
        cp = first
        while cp != None:
            if cp.idx > idx:
                return None
            if cp.idx == idx:
                return cp
            cp = cp.next
        return None
    a = is_in_list(first,idx)
    if a != None:
        return a
    #wartosc domyslna w -1 elemencie
    return first.val

def wypisz(first):
    bef = first.next
    while bef != None:
        print(bef)
        bef = bef.next

a = init()
for i in range(10):
    insert(a,10-i,i+1)
wypisz(a)
