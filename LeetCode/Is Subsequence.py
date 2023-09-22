# 2 testcases failed but accepted by other CP solution

s = "abc"
t = "ahbgdc"

# s = "axc"
# t = "ahbgdc"

# s = "acb"
# t = "ahbgdc"

# s = "aaaaaa"
# t = "vaaa"

# k = []
# t = list(t)
# for i in s:
#     if i in t:
#         k.append(t.index(i))
#         t.remove(i)
#     else:
#         print(False)
#         break
# print(k)
s = "aaaaaa"
t = "bbaaaa"

s = "ab"
t = "baab"
if len(s) > len(t):
    print(False, "over length")
elif len(s) >= 1:
    for i in s:
        if i not in t or t.count(i) < s.count(i):
            print(False, " not there")
            break
    
    k = [t.find(s[0])]
    j = 0
    for i in range(1, len(s)):
        while t.find(s[i]) < k[-1]:
            print(False, "greater")
        else:
            k.append(t.find(s[i]))