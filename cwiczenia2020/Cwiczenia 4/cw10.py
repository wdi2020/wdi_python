def cw10(t):
    MAX = len(t)
    
    is_row = True
    is_column = True
    i = 0
    while i<MAX:
        is_column = True
        is_row = True
        j=0
        while j<MAX:
            if is_row:
                if t[i][j] == 0:
                    is_row = False
            if is_column:
                if t[j][i] == 0:
                    is_column = False
            if not(is_column and is_row):
                break
            j+=1
        if is_column or is_row:
            return False
        i+=1
    return True

if __name__ == "__main__":
    print(cw10([[0 for _ in range(10)]for _ in range(10)]))