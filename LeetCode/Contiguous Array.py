"""
Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

Constraints:
1 <= nums.length <= 105
nums[i] is either 0 or 1.
"""

nums = [0, 1, 0]
# Brute force - TLE
# maxLen = 0
# for i in range(len(nums)):
#     for j in range(i+1, len(nums)+1):
#         k = nums[i:j]
#         if k.count(0) == k.count(1):
#             if len(k) > maxLen:
#                 maxLen = len(k)
#         else:
#             break
# print(maxLen)

# Using Extra Space Array
nums = [1, 0, 0, 0, 1, 1, 1, 0]
arr = [-2] * (2 * len(nums) + 1)
arr[len(nums) - 1] = -1
maxlen = 0
count = 0

for i in range(len(nums)):
    if nums[i] == 0:
        count = count + -1
    else:
        count += 1
    if arr[count + len(nums) - 1] >= -1:
        maxlen = max(maxlen, i - arr[count + len(nums) - 1])
    else:
        arr[count + len(nums) - 1] = i
print(maxlen)
