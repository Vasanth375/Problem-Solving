nums = [9, 12, 5, 10, 14, 3, 10]
pivot = 10

lresult = []
rresult = []
pivotList = []

for num in nums:
    if num < pivot:
        lresult.append(num)
    elif num == pivot:
        pivotList.append(num)
    else:
        rresult.append(num)

lresult.extend(pivotList)
lresult.extend(rresult)
print(lresult)