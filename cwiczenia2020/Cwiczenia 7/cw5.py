#5. Proszę napisać funkcję, która rozdziela elementy listy odsyłaczowej do 10 list, 
#według ostatniej cyfry pola val. W drugim kroku powstałe listy należy połączyć w jedną listę odsyłaczową, 
#która jest posortowana niemalejąco według ostatniej cyfry pola val.
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

def wsz(first,wartosc):
    cp = first
    cp2 = first.next
    while cp2!=null:
        if cp2.val>=wartosc:
            break
        cp,cp2 = cp2,cp2.next
    cp.next = Node(wartosc,cp2)

def rozdziel(first):
    tab = [Node() for _ in range(10)]
    while first!=null:
        wsz(tab[first.val%10],first.val)
        first=first.next

    new_strt=Node()
    last = new_strt
    for i in tab:
        i=i.next
        last.next = i
        while i!=null:
            last=i
            i=i.next
    return new_strt.next

first = Node()
for i in range(1,1000):
    a = Node(i)
    a.next = first
    first = a
wypisz(first.next)
wypisz(rozdziel(first.next))