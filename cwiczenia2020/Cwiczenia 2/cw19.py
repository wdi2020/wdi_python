def cw19(num):
    return [[2*n+1,2*n*(n+1),2*(n**2)+(2*n)+1] for n in range(1,num+1)]

if __name__ == "__main__":
    lista = cw19(10)