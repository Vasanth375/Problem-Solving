## Find the diagonal(left and right) sum of the matrix

mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

sum = 0
points = []

## this loop iterates and finds the diagonal sum of the matrix from Upper-left to lower-right
for i in range(len(mat)):
    points.append((i, i))
    sum += mat[i][i]
##print(points)

## this loop iterates and finds the diagonal sum of the matrix from upper-right to lower-left
k = len(mat[0]) - 1
for j in range(len(mat)):
    if (j, k) not in points:
        sum += mat[j][k]
    k -= 1

print(sum)
