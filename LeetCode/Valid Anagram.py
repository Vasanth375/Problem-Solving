s = "anagram"
t = "nagaram"

s = "rat"
t = "car"

s, t = list(s), list(t)
s.sort()
t.sort()

if "".join(s) == "".join(t):
    print(True)
else:
    print(False)