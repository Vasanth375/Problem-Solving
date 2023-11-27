
from collections import defaultdict

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
ans = defaultdict(list)

# here in this solution
for s in strs:
    # creating a list of numbers 26(length of alphabets) of values 0
    count = [0] * 26
    # iterating each string of the input
    for c in s:
        # finding the index of the each character like(a-0, b-1, c-2)
        count[ord(c) - ord("a")] += 1

    # in the default dictionary of type list we just appending our string to the keys matches the count list
    ans[tuple(count)].append(s)
print(ans.values())

# My Solution
# strs = ["a"]
defDic = defaultdict(int)

k = []
for i in range(len(strs)):
    l = [strs[i]]
    if defDic[strs[i]] != 1:
        defDic[strs[i]] = 1
        for j in range(i + 1, len(strs)):
            if (sorted(strs[i]) == sorted(strs[j])):
                l.append(strs[j])
                defDic[strs[j]] = 1
        k.append(l)
k.reverse()
print(k)
