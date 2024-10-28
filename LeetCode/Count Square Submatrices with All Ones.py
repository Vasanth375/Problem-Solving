matrix = [
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
matrix = [
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
dp=[]
sum1 = 0
row, col = len(matrix), len(matrix[0])
dp = [[0] * (col + 1) for _ in range(row + 1)]

# for i in range(len(matrix)):
#     dp[0][i] = matrix[0][i]
# for j in range(len(matrix)):
#     dp[j][0] = matrix[j][0]
for i in range(row):
    for j in range(col):
        if matrix[i][j]:
            dp[i+1][j+1] = (min(dp[i][j+1], dp[i+1][j], dp[i][j]) + 1)
            sum1 += dp[i+1][j+1]
print(sum1)
