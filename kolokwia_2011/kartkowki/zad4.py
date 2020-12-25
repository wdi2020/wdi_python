null = None


class Node:
    def __init__(self, value=null, next=null):
        self.val = value
        self.next = next

    def __str__(self):
        return f"{self.val}-->"



# reprezentacja bianrna
# niskobitowa <8
# sredniobitowa >=0 <=24
# wysokobitowa >24

def jaka_bitowo(num):
    # 0 to nisko
    # 1 to srednio
    # 2 to wysoko
    cnt = 0
    while num != 0:
        if num % 2 == 1:
            cnt += 1
        num //= 2
    return cnt


def rozdziel(first):
    first_nisko = Node(0, null)
    curr_nisko = null

    first_srednio = Node(0, null)
    curr_srednio = null

    first_wysoko = Node(0, null)
    curr_wysoko = null
    cp = first
    while cp != null:
        ret = jaka_bitowo(cp.val)
        if ret < 8:
            if curr_nisko != null:
                curr_nisko.next = Node(cp.val, null)
                curr_nisko = curr_nisko.next
            else:
                curr_nisko = Node(cp.val,null)
                first_nisko.next = curr_nisko
        elif ret > 24:
            if curr_wysoko != null:
                curr_wysoko.next = Node(cp.val, null)
                curr_wysoko = curr_wysoko.next
            else:
                curr_wysoko = Node(cp.val,null)
                first_wysoko.next = curr_wysoko
        else:
            if curr_srednio!= null:
                curr_srednio.next = Node(cp.val, null)
                curr_srednio = curr_srednio.next
            else:
                curr_srednio = Node(cp.val,null)
                first_srednio.next = curr_srednio
        cp = cp.next
    wartownik = first_nisko.next
    del first_nisko
    if wartownik == null:
        wartownik = first_srednio.next
    else:
        curr_nisko.next = first_srednio.next
    del first_srednio
    if wartownik == null:
        wartownik = first_wysoko.next
    else:
        if curr_srednio != null:
            curr_srednio.next = first_wysoko.next
        else:
            curr_nisko.next = first_wysoko.next
    del first_wysoko

    return wartownik


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

    def is_empty(self):
        return self.first == null


def tabToLista(tab: list):
    ret = lista()
    for e in tab[::-1]:
        ret.first = Node(e, ret.first)
    return ret


tab = [0, 1, 2, 1111111111111111111, 4, 511, 6, 7, 8, 12, 5]
print(lista(rozdziel(tabToLista(tab).first)))
