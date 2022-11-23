s = "qwertyuiopasdfghjklzxcvbnm"
data = {}
n = 0
s1 = []

for i in s:
    if i not in s1:
        s1.append(i)

for i in range(len(s1)):
    data.update({s1[i]:s.count(s1[i])})
# print(data)
for i in s1:
    if data.get(i) <= 1:
        del data[i]

# print(data)

finaldict = sorted(data.items(), key = lambda x:x[1] , reverse=True)
# print(finaldict)

for i in finaldict:
    for x in i:
        print(x, end=" ")
    print()