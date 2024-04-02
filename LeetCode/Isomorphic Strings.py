s = "egg"
t = "add"

mapST, mapTS = {}, {}

for i in range(len(s)):
    c1, c2 = s[i], t[i]

    if ((c1 in mapST and c2 != mapST[c1])
            or (c2 in mapTS and c1 != mapTS[c2])):
        print(False)

    mapST[c1] = c2
    mapTS[c2] = c1
print(True)
