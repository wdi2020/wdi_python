#n! by KM
from time import time
def ostatni_z_silnii(n):
    x = 5
    z = 0
    d = 1
    while(x<=n):
            z+=n//x
            x=x*5
    while(n>1):
            d=d*n%(10**(z+1))
            n=n-1
    d=d//(10**z)
    print(d)

if __name__ == "__main__":
    start = time()
    print(ostatni_z_silnii(1005))
    print(time() - start)