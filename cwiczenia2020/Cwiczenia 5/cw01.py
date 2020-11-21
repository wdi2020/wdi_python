def nwd(a,b):
    a,b = abs(a),abs(b)
    while b != 0:
        b,a = a%b,b
    #end while
    return a
#end def nwd 
def nww(a,b):
    return (a*b)/nwd(a,b)
def mnozenie(ulamek1,ulamek2):
    ret = (ulamek1[0]* ulamek2[0],ulamek2[1] * ulamek1[1])
    return skracanie(ret)
def dodawanie(ulamek1,ulamek2):
    nw = nww(ulamek1[1],ulamek2[1])
    return skracanie(((ulamek1[0]* (nw//ulamek1[1])) + (ulamek2[0]* (nw//ulamek2[1])),nw))
def odejmowanie(ulamek1,ulamek2):
    minus_2 = (ulamek2[0] *-1, ulamek2[1])
    return dodawanie(ulamek1,minus_2)
def dzielenie(ulamek1,ulamek2):
    odwrocenie = (ulamek2[1],ulamek2[0])
    return mnozenie(ulamek1,odwrocenie)
def potegowanie(a,b):
    return ((a[0]**b[0]) * (1/b[1])) / ((a[1]**b[0])**1/b[1])
def skracanie(ulamek1):
    nw = nwd(ulamek1[0],ulamek1[1])
    return (ulamek1[0]//nw,ulamek1[1]//nw)
def print_ul(ul):
    print(f"{ul[0]} / {ul[1]}")
