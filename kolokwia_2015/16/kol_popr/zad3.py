# Zad.3 Dany jest zbiór punktów płaszczyzny o współrzędnych będących liczbamicałkowitymi.7bior
# ten dany jest w postaci listy jednokierunkowej. Proszę funkcję, która rozdziela łańcuch na cztery
# łańcuchy zawierające punkty należące odpowiednio do l,ll,lll i lV ćwiartki układu współrzędnych,
# natomiast punkty leżące na osiach układu współrzędnych usuwa z pamięci. Proszę zadeklarować
# odpowiednie typy.
null = None


class lista:
    def __init__(self, first=null):
        self.first = first

    def __str__(self):
        cp = self.first
        cp2 = self.first.next
        if cp == null:
            return "List is empty!"
        ret = str(cp)
        while null != cp2:
            ret = ret + str(cp2)
            cp2 = cp2.next
        return ret


class Node:
    # val,next,idx
    def __init__(self, x, y, next=None):
        self.next = next
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x},{self.y})-->"

    def get_cwiara(self):
        if self.x == 0 or self.y == 0:
            return 0
        if self.x > 0:
            if self.y > 0:
                return 1
            else:
                return 4
        else:
            if self.y > 0:
                return 2
            else:
                return 3


def tabToLista(tab: list):
    ret = lista()
    for e in tab[::-1]:
        ret.first = Node(e[0], e[1], ret.first)
    return ret


def check(first: Node):
    cw1 = null
    cw2 = null
    cw3 = null
    cw4 = null
    cp = first
    while cp != null:
        a = cp.get_cwiara()
        if a == 0:
            first = cp.next
            del cp
        elif a == 1:
            if cw1 == null:
                cw1 = cp
                first = cp.next
                cp.next = null
            else:
                first = cp.next
                cp.next = cw1
                cw1 = cp
        elif a == 2:
            if cw2 == null:
                cw2 = cp
                first = cp.next
                cp.next = null
            else:
                first = cp.next
                cp.next = cw2
                cw2 = cp
        elif a == 3:
            if cw3 == null:
                cw3 = cp
                first = cp.next
                cp.next = null
            else:
                first = cp.next
                cp.next = cw3
                cw3 = cp
        elif a == 4:
            if cw4 == null:
                cw4 = cp
                first = cp.next
                cp.next = null
            else:
                first = cp.next
                cp.next = cw4
                cw4 = cp
        cp = first
    print(lista(cw1))
    print(lista(cw2))
    print(lista(cw3))
    print(lista(cw4))


tab = [(1, 0), (2, 2), (-1, 2), (9, 0), (1, -2), (-3, -3), (0, 1)]
check(tabToLista(tab).first)
