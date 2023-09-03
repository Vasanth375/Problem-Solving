def uniquePaths(m: int, n: int):
    '''Dynamic Programming used to store total number of moves travelled from [0][0] to [m][n] from all sides
    '''
    dp = [[0] * n for _ in range(m)]
    for r in range(m):
        for c in range(n):
            if r == 0 or c == 0:
                dp[r][c] = 1
            else:
                dp[r][c] = dp[r-1][c] + dp[r][c-1]
    print(dp)
    return dp[m-1][n-1]

print(uniquePaths(3, 7))

