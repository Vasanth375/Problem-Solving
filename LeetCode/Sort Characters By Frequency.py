# Time Limit Exceeded
# 31 / 33 testcases passed

s = "tree"
s = "raaeaedere"
s = "cccaaa"
s = "Aabb"
newList = []
valuesList = []
ss = list(set(s))
for i in range(len(ss)):
    k = [ss[i]]
    for j in range(len(s)):
        if s[j] in k:
            k.append(s[j])
    newList.append(k[:-1])
    valuesList.append(len(k[:-1]))

sortedVal = valuesList.copy()
sortedVal.sort(reverse=True)
# print(valuesList)
# print(sortedVal)

newS = ""
for i in sortedVal:
    k = valuesList.index(i)
    valuesList[k] = -1
    newS += "".join(newList[k])
print(newS)
