## I've found Three Approaches for this problem
# 1. Normal Dictionary
# 2. Bucket sorting Method using dictionary
# 3. find all the occurances of a character and store it in a list
#   return new string based on the descending order of the list item

from collections import Counter, defaultdict

s = "tree"
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

newS = ""
for i in sortedVal:
    k = valuesList.index(i)
    valuesList[k] = -1
    newS += "".join(newList[k])


# Approach: 
# sort our hashmap in reverse order
freq = Counter(s)

# for sorting there are 3 parameters essentialy 
freq = sorted(freq.items(), key = lambda  x: x[1], reverse = True)

ans = ""

for key, value in freq:
    ans += key*value

## Through Bucket Sorting Approach
counter = Counter(s)
buckets = defaultdict(list)
for char, num in counter.items():
    buckets[num].append(char)

res = ""
for i in range(len(s), 0, -1):
    for c in buckets[i]:
        res += c * i