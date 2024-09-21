n= 13
l = []
for i in range(1, n+1):
    l.append((i))
l.sort(key=lambda x: str(x))
print(l)
