nums = [2, 2, 3, 4]
# nums = [4, 2, 3, 4]


nums.sort()
count = 0

for k in range(len(nums)-1, 1, -1):
    left = 0
    right= k-1
    while left < right:
        if nums[left] + nums[right] > nums[k]:
            count += right - left   # counting all triplets with the current k
            right -= 1
        else:
            left += 1
print(count)

# for i in range(len(nums)):
#     for j in range(i+1, len(nums)):
#         for k in range(j+1, len(nums)):
#             if nums[i] + nums[j] > nums[k]:
#                 count += 1
#             else:
#                 break

# left = 0
# right = len(nums)-1
# while left < right:
#     mid = (left + right)//2
#     if (nums[left]+nums[mid] > nums[right]):
#         count += 1
#         left += 1
#     right -= 1
#     # elif (nums[right]+nums[mid] > nums[left]):
#     #     count += 1
#     # elif (nums[left]+nums[right] > nums[mid]):
#     #     count += 1
#     # elif (nums[right]+nums[left] > nums[mid]):
#     #     count += 1