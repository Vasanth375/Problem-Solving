# Best Example for DP and Memoization

s = "bbbab"
n = len(s)

dp = [[0] * n for _ in range(n)]

## Examine the pattern
for i in range(n-1, -1, -1):
    dp[i][i] = 1
    for j in range(i+1, n):
        if s[i] == s[j]:
            dp[i][j] = dp[i+1][j-1] +2
        else:
            dp[i][j] = max(dp[i+1][j], dp[i][j-1]) # type: ignore
print(dp[0][n-1])   