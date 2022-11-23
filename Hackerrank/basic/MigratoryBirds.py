arr = [1,4,4,4,5,3]
arr = [1,1,2,2,3]
highBird = max(arr)
countBirds = dict()
for i in range(1,highBird+1):
    countBirds[i] = arr.count(i)
#print(countBirds)

maxFrequency = list(countBirds.keys())
values = list(countBirds.values())
print(maxFrequency[max(values)])
