x = 3
y = 4
s = "00000"

cost = []
for i in range(len(s)):
    k = s.count("10")
    l = s.count("01")
    cost.append((k * y) + (l * x))
    s = s[-1] + s[: len(s) - 1]
    print(s)
print(cost)
