# Minimization problem
s = "0100"
s = "10"
# s = "1111"
# s = "10010100"
S0, S1 = 0, 0
for i in range(len(s)):
    if i % 2 == 0:
        if s[i] == '0':
            S1 += 1
        else:
            S0 += 1
    else:
        if s[i] == '1':
            S1 += 1
        else:
            S0 += 1
print(min([S0, S1]))
