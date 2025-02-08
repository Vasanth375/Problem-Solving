from collections import defaultdict

limit = 4
queries = [[1, 4], [2, 5], [1, 3], [3, 4]]
# limit = 4
# queries = [[0, 1], [1, 2], [2, 2], [3, 4], [4, 5]]

k = {}
color_count = defaultdict(int)
distinct_colors = 0
res = []

for i, j in queries:
    if i in k:
        old_color = k[i]
        color_count[old_color] -= 1
        if color_count[old_color] == 0:
            distinct_colors -= 1
    k[i] = j
    if color_count[j] == 0:
        distinct_colors += 1
    color_count[j] += 1
    res.append(distinct_colors)

print(res)