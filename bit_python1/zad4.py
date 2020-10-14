from random import randint
#NA BIT PYTHON Z 27.09

def main():
    n = int(input("podaj n:"))
    m = int(input("podaj m:"))
    matrix = [[randint(0,255) for _ in range(m)] for _ in range(n)] 
    while True:
        st = input("Podaj komende:")
        # "flip horizontal" - odbicie w osi poziomej:
        if st == "flip horizontal":
            for i in range(n):
                matrix[i] = [matrix[i][m-j-1] for j in range(0,m)]
        # "flip vertical" - odbicie w osi pionowej:
        elif st == "flip vertical":
            for i in range(m):
                for j in range(n//2):
                    buff = matrix[j][i]
                    matrix[j][i] = matrix[n-1-j][i]
                    matrix[n-1-j][i] = buff
        # "rotate left" - obrót o 90 stopni w lewo:
        elif st == "rotate left":
            new_matrix = [[0 for _ in range(n)] for _ in range(m)] 
            for i in range(n):
                for j in range(m):
                    new_matrix[j][i] = matrix[i][j]
            matrix = new_matrix
            for i in range(m):
                for j in range(n//2):
                    buff = matrix[j][i]
                    matrix[j][i] = matrix[n-1-j][i]
                    matrix[n-1-j][i] = buff
        # "rotate right" - obrót o 90 stopni w prawo:
        elif st == "rotate right":
            new_matrix = [[0 for _ in range(n)] for _ in range(m)] 
            for i in range(n):
                for j in range(m):
                    new_matrix[i][j] = matrix[j][i]
            matrix = new_matrix
            for i in range(n):
                matrix[i] = [matrix[i][m-j-1] for j in range(0,m)]
        # "reverse values" - interpretujemy wartości jako odcienie szarości, tj. 0 to czarny, a 255 to biały; odbicie takiego obrazu to zamiana 0 na 255, 255 na 0, 1 na 254, 254 na 1 i tak dalej:
        elif st == "reverse values":
            matrix = [[255 - matrix[i][j] for i in range(n)] for j in range(m)]
        elif st == "done":
            for i in range(n):
                print(matrix[i])
            break



if __name__ == "__main__":
    main()