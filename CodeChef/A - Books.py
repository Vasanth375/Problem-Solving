n = 4
a = [1, 2, 4, 4]

n, a = 5, [1, 2, 2, 2, 2]

a.sort()
k = []
for i in range(n):
    count = 0
    for j in range(i + 1, n):
        if a[i] < a[j]:count += 1
    k.append(count);count = 0

print(*k)


### simplified version of outer loop with minimal number of iterations
# k = a.copy()
# k = set(k)

# l = []
# for i in k:
#     count = 0
#     for j in a:
#         if i < j:
#             count += 1
#     l.append(count)
#     count = 0
# lenK = len(k)
# l.extend([0] * (n - lenK))
# print(*l)
