arr = [1,4,4,4,5,3]
arr = [1 ,2 ,3 ,4 ,5 ,4 ,3 ,2 ,1 ,3 ,4]
arr = [2 ,4 ,3 ,2 ,3 ,1 ,2 ,1 ,3 ,3]
highBird = max(arr)
countBirds = dict()
for i in range(1,6):
    countBirds[i] = arr.count(i)

values = list(countBirds.values())

maxValue = max(values)
l = dict()
for i in range(1, 6):
    if countBirds[i] == maxValue:
        l[i] = countBirds[i]

for i in l:
    print(i)