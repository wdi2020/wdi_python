#NA BIT PYTHON Z 27.09

def zad1():
    tablica = []
    string = 'GATATATGCATATACTT'
    substring = 'ATAT'
    for i in range(0,len(string)-len(substring) + 1):
        for j in range(0,len(substring)):
            if substring[j] != string[i+j]:
                break
            elif j == len(substring)-1:
                tablica.append(i)
    print(f"{len(tablica)} occurences")
    for i in tablica:
        print(i+1,end=" ")

            
if __name__ == "__main__":
    zad1()