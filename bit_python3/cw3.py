def get_pages(my,others):
    my_pages = dict()
    recommended = dict()
    with open(my) as my_file:
        for line in my_file:
            my_pages = line.split(" -> ")[1].split(",")
            my_pages = [elem.strip() for elem in my_pages]
    
    with open(others) as file:
        for line in file:
            temp_pages = [elem.strip() for elem in line.split(" -> ")[1].split(",")]
            for e in my_pages:
                if e in temp_pages:
                    for page in temp_pages:
                        if e != page:
                            if not page in recommended:
                                recommended[page] = 1
                            else:
                                recommended[page] = recommended[page] + 1
                    break
    
    recommended_sorted =  {k: v for k,v in sorted(recommended.items(), key=lambda item : item[1])}
    return list(recommended_sorted)[-1:-6:-1]

if __name__ == "__main__":
    print(get_pages('me.txt','others.txt'))