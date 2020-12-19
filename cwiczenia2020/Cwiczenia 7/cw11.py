null= None
class Node:
    #val,next
    def __init__(self,val=0,next=null):
        self.next = next
        self.val = val
    def __str__(self):
        return f"{self.val}-->"
def wypisz(first):
    while first != null:
        print(first,end='')
        first = first.next
    print()
#11. Lista zawiera niepowtarzające się elementy. Proszę napisać funkcję do
#której przekazujemy wskaźnik na początek oraz wartość klucza. Jeżeli
#element o takim kluczu występuje w liście należy go usunąć z listy. Jeżeli 
#elementu o zadanym kluczu brak w liście należy element o takim kluczu
#wstawić do listy.
def insertIfNotInList(first,key):
    if first==null:
        return Node(key)
    cp=first
    while cp.next!=null:
        if key==cp.val:
            return first
        cp=cp.next
    if key==cp.val:
        return first
    cp.next = Node(key)
    return first

first = Node(9)
for i in range(2,7):
    a = Node(i,first)
    first = a
wypisz(first)
wypisz(insertIfNotInList(first,100))
