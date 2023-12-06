n = 20

ans = 0
mon = 1
while n > 0:
    for day in range(min(n, 7)):
        ans += mon + day
    n -= 7

    mon += 1
print(ans)
