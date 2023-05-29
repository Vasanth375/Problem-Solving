a = "abcabc"

n = len(a) // 2

A = a[:n]
B = a[n:]
if (A + B) == a and (B + A) == a:
    print("YES")
else:
    print("NO")
