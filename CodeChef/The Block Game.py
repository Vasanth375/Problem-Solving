a = "999"

a = list(a)

k = a.copy()
k.reverse()
if "".join(a) == "".join(k):
    print(True)
else:
    print(False)
