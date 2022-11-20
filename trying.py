def ADDSTR():
    a = [{1: "one", 2: "two", 3: "three"},{1: "one", 2: "two", 3: "three"},{1: "one", 2: "two", 3: "three"},{1: "one", 2: "two", 3: "three"}]
    z = ''
    sp = a[0]
    print(sp)
    sp.pop(1)
    names = list(sp.keys())
    print(names)
    for i in names:
        if i == names[len(sp.keys())-1]:
            i = str(i)
            z = z + i
        else:    
            i = str(i)
            z = z + i + ','
    return z
print(ADDSTR())

    

        