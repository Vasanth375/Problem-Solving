matrix = [[1,2,3],[4,5,6],[7,8,9]]
n = len(matrix)

# Brute Force Approach
# a = [[0]*n for _ in range(n)]
# n = n - 1
# for i in range(n+1):
#     for j in range(n+1):
#         a[j][n-i] = matrix[i][j]
# print(a)

# Optimal Approach
# Matrix transpose and reverse each sub list
n = len(matrix)
sett = []
for i in range(n):
    for j in range(n):
        k = [i,j]
        k.sort()
        if k not in sett:
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            sett.append(k)

for i in matrix:
    i.reverse()
print(matrix)