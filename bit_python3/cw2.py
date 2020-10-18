import os
def get_text(nazwa):
    for file in os.listdir():
        if nazwa in file and file.endswith(".txt"):
            czesci_nazwy = file[:-4].split("_")
            index = czesci_nazwy.index(nazwa)
            with open(file,"r") as content:
                text = content.read().split("\n---EOF---\n")
            return text[index]
# "\n---EOF---\n"




if __name__ == "__main__":
    print(get_text("blackwhitetree"))