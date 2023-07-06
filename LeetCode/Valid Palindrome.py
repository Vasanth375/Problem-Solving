s = "A man, a plan, a canal: Panama"
s = "race a car"
s = s.lower()
s = s.replace(" ", "")

k = ""
for i in s:
    if i.isalnum():
        k += i

k = list(k)
m = list(k)

m.reverse()
if m == k:
    print(True)
else:
    print(False)