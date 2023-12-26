s = "10"
s = "0226"
# Dynamic programming with iterating approach
dp = {len(s): 1}

# Iterating in reverse order over the length of s to 0
for i in range(len(s)-1, -1, -1):
    # if string start with 0 it's invalid one
    if s[i] == "0":
        dp[i] = 0
    else:
        # if not zero set previous value of the i+1 to i
        dp[i] = dp[i+1]

    # checking if Ith index is 1 or 2 because there are only 26 alphabets to max value is 2 of first digit and 6 is for second digit
    if (i+1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i+1] in "0123456")):
        dp[i] += dp[i+2]
print(dp[0])

# Dynamic programming with Recursive approach
s = "10"
dp = {len(s): 1}


def dfs(i):
    if i in dp:
        return dp[i]

    if s[i] == "0":
        return 0

    ans = dfs(i+1)
    if (i+1 < len(s) and (s[i] == "1" or
                          s[i] == "2" and s[i+1] in "0123456")):
        ans += dfs(i+2)
    dp[i] = ans
    return ans


print(dfs(0))
