# 3. Dane są deklarację reprezentujące listę z klockami mag-mina (patrz zadanie 2).
# struct klocek {
# int a;
# int b;
# klocek *next;
# };
# Lista zawiera zestaw klocków, które można ułożyć w ciąg. Niestety klocki pomieszały się. Proszę napisać funkcję,
# która ustawia klocki na liście w ciąg. Uwaga: orientacja klocków w liście jest właściwa.
# Na przykład listę: [2|9] [3|6] [8|2] [2|3] [6|2]
# należy przekształcić na listę: [8|2] [2|3] [3|6] [6|2] [2|9]
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


class klocek:
    # val,next,idx
    def __init__(self, a, b, next=None):
        self.next = next
        self.a = a
        self.b = b

    def __str__(self):
        return f"{self.a}|{self.b}-->"


def tabToLista(tab: list):
    ret = lista()
    for e in tab[::-1]:
        ret.first = klocek(e[0], e[1], ret.first)
    return ret


def check(lis):
    def reku(left, current):
        if left == null:
            return current
        cp, cp2 = null, left
        while cp2 != null:
            if cp2.b == current.a:
                if cp == null:
                    temp = cp2.next
                    cp2.next = current
                else:
                    cp.next = cp2.next
                    cp2.next = current
                    temp = left

                ret = reku(temp, cp2)
                if ret != null:
                    return ret

                if cp == null:
                    current = cp2.next
                    cp2.next = temp
                else:
                    current = cp2.next
                    cp2.next = cp.next
                    cp.next = cp2
            cp, cp2 = cp2, cp2.next
        return null

    cp, cp2 = null, lis
    left = null
    while cp2 != null:
        if cp == null:
            left = cp2.next
            cp2.next = null
            ret = reku(left, cp2)
            if ret != null:
                return ret
            cp2.next = left
        else:
            left = lis
            cp.next = cp2.next
            temp = cp2.next
            cp2.next = null
            ret = reku(left, cp2)
            if ret != null:
                return ret
            cp.next = cp2
            cp2.next = temp
        cp, cp2 = cp2, cp2.next


# Na przykład listę: [2|9] [3|6] [8|2] [2|3] [6|2]
# należy przekształcić na listę: [8|2] [2|3] [3|6] [6|2] [2|9]
tab1 = [(2, 9), (3, 6), (8, 2), (2, 3), (6, 2)]
print(lista(check(tabToLista(tab1).first)))
