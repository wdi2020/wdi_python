#7. Proszę napisać funkcję usuwającą ostatni element listy. Do funkcji
#należy przekazać wskazanie na pierwszy element listy.
null= None
class Node:
    #val,next
    def __init__(self,val=0,next=null):
        self.next = next
        self.val = val
    def __str__(self):
        return f"{self.val}--->"
def wypisz(first):
    while first != null:
        print(first,end='')
        first = first.next
    print()

def pop_back(first):
    if first==null:
        return null
    cp = first
    cp2=first.next
    while cp2.next!=null:
        cp,cp2=cp2,cp2.next
    cp.next = null
    del cp2
    return first

first=Node()
for i in range(10):
    a = Node(i+1)
    a.next = first
    first = a
wypisz(first)
for i in range(9):
    wypisz(pop_back(first))