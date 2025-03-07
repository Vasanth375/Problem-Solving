s1 = "abc"
s2 = "bbca"


sortedS1 = sorted(s1)
sortedS1 = "".join(sortedS1)

for s22 in range(len(s2)):
    if s2[s22] in s1:
        # k = s2[s2.index(s22):s2.index(s22)+len(s1)]
        k = s2[s22:s22+len(s1)]
        sortedK = sorted(k)
        sortedK = "".join(sortedK)
        if sortedK == sortedS1:
            print(True)
            break
print(False)