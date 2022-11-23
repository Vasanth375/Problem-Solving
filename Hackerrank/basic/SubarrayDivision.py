# only one test case passed

from itertools import permutations, combinations

#s = [2 ,5 ,1 ,3 ,4 ,4 ,3 ,5 ,1 ,1 ,2 ,1 ,4 ,1 ,3 ,3 ,4 ,2 ,1]
s = [2,2,1,3,2]
d = 4
m = 2

# s = [4]
# d = 4
# m = 1
# x = list(set(combinations(s,m)))
x = []
# for i in range(len(s)-1):
#     x.append((s[i], s[i+1]))

# count = 0
# for i in x:
#     if sum(i) == d:
#         count+=1
# print(x, count)

results = 0
for index, item in enumerate(s):
    total = 0
    
    if index + m > len(s): break

    for window_index in range(m):
        total += s[index + window_index]
    if total == d:
        results +=1
print(results)