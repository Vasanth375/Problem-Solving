nums = [1,3,4,2,2]

setNums = set()

for i in nums:
    if i in setNums:
        print(i)
        break
    setNums.add(i)
