matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# matrix = [[1, 2, 3], [4, 5, 6]]
res = []
for i in range(len(matrix[0])):
    k = []
    for j in range(len(matrix)):
        k.append(matrix[j][i])
    res.append(k)
print(res)
