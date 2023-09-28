nums = [3,1,2,4]

nums = [0]
even = []
odd = []
for i in nums:
    if i%2 == 0:
        even.append(i)
    else:
        odd.append(i)
print(even+odd)