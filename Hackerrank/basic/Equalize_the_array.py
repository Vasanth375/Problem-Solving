arr = [3, 3, 2, 1, 3]
countList = []
for i in set(arr):
    countList.append(arr.count(i))
print(len(arr)-max(countList))