#NA BIT PYTHON Z 27.09

from os import mkdir
from os import listdir
from shutil import move
def main():
    mkdir("images")
    mkdir("films")
    mkdir("photos")
    mkdir("docs")
    mkdir("music")
    for file in listdir("."):
        #mp4
        if file[-4:] == ".mp4":
            move(file,f"films\\{file}")
        #.png, .jpg
        elif file[-4:] == ".png" or file[-4:] == ".jpg": 
            move(file,f"photos\\{file}")
        # mp3
        elif file[-4:] == ".mp3":
            move(file,f"music\\{file}")
        # .doc, .docx, .odt, .pdf
        elif file[-4:] == ".doc" or file[-5:] == ".docx" or file[-4:] == ".odt" or file[-4:] == ".pdf": 
            move(file,f"docs\\{file}")

if __name__ == "__main__":
    main()