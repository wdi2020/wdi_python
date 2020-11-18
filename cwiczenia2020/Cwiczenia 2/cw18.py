#cw 18
def cw18():
    a0,a1 = 0,1
    b0 = 2
    a2 = a1 - (b0 * a0)
    b1 = b0 + (2 * a1)
    while int(input(">")) == a0:
        print(b0)
        a0,a1,b0,a2,b1 = a1,a2,b1,a1 - (b0 * a0),b0 + (2 * a1)

if __name__ == "__main__":
    cw18()