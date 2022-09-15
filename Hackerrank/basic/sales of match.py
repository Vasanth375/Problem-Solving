'''
1) given a list of elements
2) in the list count from 0 if two elements are same then increment k value by 1 and remove 
    remaining same equal elements where in the list.
'''
# run code

ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
# ar = [1,2,1,2,1,3,2]
countDict = dict()

for i in ar:
    countDict[i] = ar.count(i)

finalList = []
for i in countDict:
    for j in range(countDict[i]+1):
        if j % 2 == 0:
            if j != 0:
                finalList.append([j])

print(len(finalList))