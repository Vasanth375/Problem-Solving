## ACCEPTED
candies = [2,3,5,1,3]
extraCandies = 3

candies = [4,2,1,1,2]
extraCandies = 1

candies = [12,1,12]
extraCandies = 10

boool = []
for i in range(len(candies)):
    count = 0
    for j in range(len(candies)):
        if i != j:
            if candies[i] + extraCandies >= candies[j]:
                count+=1
    if count == len(candies)-1:
        boool.append(True)
    else:
        boool.append(False)

print(boool)