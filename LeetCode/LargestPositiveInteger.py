# passed
nums = [-1,2,3,-3, -2]
nums = [-1,10,6,7,-7,1]
nums = [-10,8,6,7,-2,-3]

negArr = [i for i in nums if i<0]
posArr = [i for i in nums if i>0]
finalArray = []
for i in reversed(posArr):
    if -i in nums:
        finalArray.append(i)

if finalArray:
    print(max(finalArray))
else:
    print(-1)