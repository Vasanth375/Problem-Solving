nums = [1,2,1]
nums = [1,2,3,4,3]
n = len(nums)
nge = []

# O(n*(r+l))
for i in range(n):
    k = nums[i]
    l = nums[0:i]
    r = nums[i+1: n]
    found = False
    for j in r:
        if j > k:
            nge.append(j)
            found = True
            break
    if not found:
        for j in l:
            if j > k:
                nge.append(j)
                found = True
                break
    if not found:
        nge.append(-1)


# stack = []
# n = len(nums)
# nums = nums + nums
# nge = [-1]*n
# for i in range(len(nums)-1, -1, -1):
#     while stack and stack[-1] <= nums[i%n]:
#         stack.pop()
#     if i < n:
#         if stack:
#             nge[i] = stack[-1]
#         else:
#             nge[i] = -1
#     stack.append(nums[i%n])
# print(nge)