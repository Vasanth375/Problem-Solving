a = [[140, 82], [589, 134], [90, 110], [112, 106], [88, 90]]

k = 0
l = 0
maxi = 0
s1, s2 = 0, 0
for m in a:
    s1 += m[0]
    s2 += m[1]
    l = abs(s1 - s2)
    if l > maxi:
        maxi = l
        k = 1 if s1 > s2 else 2
    
print(k, maxi)
