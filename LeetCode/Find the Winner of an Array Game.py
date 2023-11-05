# from collections import defaultdict

# arr = [2,1,3,5,4,6,7]
# k = 2
# arr = [3,2,1]
# k = 10

# n = 0
# m = defaultdict(int)
# while  n != 2:
#     if arr[0] > arr[1]:
#         m[arr[0]] += 1
#         i = arr.pop(1)
#         arr.append(i)
#     else:
#         m[arr[1]] += 1
#         i = arr.pop(0)
#         arr.append(i)
#     if k in m.values():
#         n = 2

# for i in m:
#     if m[i] == k:
#         print(i)
#         break

from sympy import true


arr = [2,1,3,5,4,6,7]
k = 2
# arr = [3,2,1]
# k = 10

# using Queue
winstreak = 0
maxElement = max(arr)
queue = arr[1:]
curr = arr[0]

while True:
    opponent = queue.pop(0)
    if curr > opponent:
        queue.append(opponent)
        winstreak += 1
    else:
        queue.append(curr)
        curr = opponent
        winstreak = 1
    if winstreak == k or curr == maxElement:
        print(curr)
        break
