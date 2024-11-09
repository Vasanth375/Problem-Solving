'''
1. Each element of the array should be obtained by “merging” x and v where v = 0, 1, 2, …(n - 1).
2. To merge x with another number v, keep the set bits of x untouched, for all the other bits, 
fill the set bits of v from right to left in order one by one.
3. So the final answer is the “merge” of x and n - 1.
'''

import collections

n = 11
x = 7
n = 3
x = 4


# n = 6715154
# x = 7193485

n -= 1
bn = collections.deque(bin(n)[2:][::-1])
bx = bin(x)[2:][::-1]

ans = []

for c in bx:
    if c == '1':
        ans.append('1')
    else:
        if len(bn) >0:
            ans.append(bn.popleft())
        else:
            ans.append("0")
while len(bn) > 0:
    ans.append(bn.popleft())
print(int("".join(ans[::-1]),2))