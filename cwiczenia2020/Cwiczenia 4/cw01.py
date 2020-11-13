def cw01():
    MAX = 7 
    d,g,l,p = MAX-1,0,0,MAX-1
    t = [[0 for _ in range(MAX)] for _ in range(MAX)]
    row_index = 0
    column_index = 0
    i = 1
    for _ in range(MAX//2):
        while column_index <= p:
            t[row_index][column_index] = i
            column_index +=1
            i+=1
        g+=1
        p-=1
        column_index-=1
        row_index+=1
        while row_index <= d:
            t[row_index][column_index] = i
            row_index+=1
            i+=1
        d-=1
        row_index-=1
        column_index-=1
        while column_index >= l:
            t[row_index][column_index] = i
            column_index-=1
            i+=1
        l+=1
        column_index+=1
        row_index-=1
        while row_index >= g:
            t[row_index][column_index] = i
            row_index-=1
            i+=1
        
        row_index+=1
        column_index+=1
    if MAX%2 == 1:
        t[row_index][column_index] = i
    return t

if __name__ == "__main__":
    for i,e in enumerate(cw01()):
        print(e,i)