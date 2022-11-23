a = 10
a =  list(str(a))
#print(int("".join(list(reversed(a)))))

nums = [1,13,10,12,31]
nums = [2,2,2]
a = nums.copy()
for i in nums:
    element = list(str(i))
    a.append(int("".join(list(reversed(element)))))

print(len(set(a)))