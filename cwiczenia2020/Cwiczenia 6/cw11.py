def nki(t, s, n, pary = [], p=0):
    if n == 1:
        for i in range(p, len(t)):
            if t[i] == s and len(pary) > 0 :
                pary += [s]
                print(pary)
                pary = []
            else:
                for i in range(p,len(t)-n+1):
                    if s%t[i] == 0:
                        nki(t,s//t[i],n-1,pary+[[t[i]]],i+1)
