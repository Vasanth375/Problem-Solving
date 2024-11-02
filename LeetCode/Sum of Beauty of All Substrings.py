#10324ms
# Beats
# 12.76%
def beauty(s: str):
    ss = set(s)
    l = []
    for i in ss:
        l.append(s.count(i))
    return max(l)-min(l)

s = "aabcb"
s = "aabcbaa"
k = 0

for i in range(len(s)):
    for j in range(i+1, len(s)):
        ss = s[i:j+1]
        o = len(set(ss))
        if  o != len(ss) and o != 1:
            k += beauty(ss)
