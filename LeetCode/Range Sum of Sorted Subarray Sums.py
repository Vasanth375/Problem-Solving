# Time Complexity - O(N**2 log N)

nums = [1,2,3,4]
n = 4
left = 1
right = 10

k = []
for i in range(len(nums)):
    l = nums[i]
    k.append(l)
    for j in range(i+1, len(nums)):
        l += nums[j]
        k.append(l)
print(k)
k.sort()
print((sum(k[left-1: right])) % (10**9 + 7))