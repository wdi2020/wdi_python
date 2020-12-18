#6. Proszę napisać funkcję wstawiającą na koniec listy nowy element. Do
#funkcji należy przekazać wskazanie na pierwszy element listy oraz wstawianą
#wartość.
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

def push_back(first,wartosc):
    if first ==null:
        return Node(wartosc)
    cp =first
    cp2=first.next
    while cp2!=null:
        cp,cp2=cp2,cp2.next
    new_ = Node(wartosc)
    cp.next = new_
    return first


first = null
for i in range(10):
    first = push_back(first,i+1)
wypisz(first)