import os
def get_files():
    lista_plikow = os.listdir()
    caly_content = ""
    nazwa = ""
    for plik in lista_plikow:
        if plik.endswith(".txt"):
            with open(plik,"r") as file:
                caly_content = caly_content + file.read() + "\n---EOF---\n"
                nazwa = nazwa + plik[:-4] + "_"
    nazwa = nazwa[:-1]
    nazwa = nazwa + ".txt"
    with open(nazwa,"w+") as file:
        file.writelines(caly_content)

if __name__ == "__main__":
    get_files()