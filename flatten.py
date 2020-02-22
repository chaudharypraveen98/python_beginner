def flatten(l):
    if len(l)!=0:
        for i in l:
            while type(i)==list:
                for h in range(len(i)):
                    l.insert(l.index(i),i[h])
                l.pop(l.index(i))
                break
        print(l)
l=[]
flatten(l)