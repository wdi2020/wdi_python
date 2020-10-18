def cw13():
    # tab = [2,3,2,7,1,2,4,8,5,2,2,4,3,9,5,4,0]
    st = input("Jebne zaraz wdi za 1 dzien..:")
    tab = [int(i) for i in st.split(",")] 
    tab = tab[:-1:1]

    index = 0
    while index <= (len(tab)-1):
        srednia = 0

        count_left = 2
        count_right = 2
        curr_index_left = index - 1
        curr_index_right = index + 1
        flag_l = False
        flag_r = False


        while count_left > 0 or count_right > 0:
            if curr_index_left >= 0:
                srednia += tab[curr_index_left]
                count_left -= 1
                curr_index_left-=1
            elif not flag_l:
                count_right += count_left 
                flag_l = True
            
            if curr_index_right < len(tab):
                srednia += tab[curr_index_right]
                count_right -= 1
                curr_index_right +=1
            elif not flag_r:
                 count_left += count_right
                 flag_r = True

        if srednia / 4 == float(tab[index]):
            print(tab[index], index)

        index += 1

if __name__ == "__main__":
    print(cw13())