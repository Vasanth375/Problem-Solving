jewels = "aA"
stones = "aAAbbbb"

iHave = 0
for i in jewels:
    iHave += stones.count(i)
print(iHave)
