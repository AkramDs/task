def abbreviation(a, b):
    a = a.upper()
    b = b.upper()
    
    c = ''
    for i in range(a.__len__()):
        if a[i] in b:
            c += a[i]

    if c == b:
        return 'YES'
    else:
        return 'NO'

l = ['Pi','AfPZN', 'LDJAN', 'UMKFW', 'K', 'LIT', 'QYCH', 'DFIQG', 'sYOCa', 'JHMWY']
l2 = ['P', 'APZNC', 'LJJM', 'UMKFW', 'KXzQ', 'LIT', 'QYCH', 'DFIQG', 'YOCN', 'HUVPW']

#print(l.__len__(), l2.__len__())
for i in range(l.__len__()):
    total = abbreviation(l[i], l2[i])
    print(total)#i, total, l[i], l2[i])