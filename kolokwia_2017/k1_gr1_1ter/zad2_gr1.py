def func(tab,N):
    max_dl = 0

    curr_sum = 0
    curr_sum_ind = 0
    curr_dl = 0
    last = 0

    i = 0
    while i<N:
        if tab[i] > last:
            curr_sum += tab[i]
            curr_sum_ind += i
            curr_dl+=1
            last = tab[i]
            if curr_sum == curr_sum_ind:
                if curr_dl > max_dl:
                    max_dl = curr_dl
            else:
                copy_curr_sum = curr_sum
                copy_curr_sum_ind = curr_sum_ind
                copy_curr_dl = curr_dl
                j = i-copy_curr_dl + 1
                while j < i:
                    copy_curr_dl -=1
                    copy_curr_sum -= tab[j]
                    copy_curr_sum_ind -= j
                    if copy_curr_sum == copy_curr_sum_ind:
                        if copy_curr_dl > max_dl:
                            max_dl = copy_curr_dl
                            break
                    j+=1
        else:
            curr_sum = tab[i]
            curr_sum_ind = i
            curr_dl = 1
            last = tab[i]
        i+=1
    return max_dl


print(func([r_ for r_ in range(1000)],1000))

