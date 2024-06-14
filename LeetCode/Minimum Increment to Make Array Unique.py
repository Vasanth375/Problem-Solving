nums = [3,2,1,2,1,7]
# nums = [1,2,2]
# setNums = []

# m = 0
# for i in nums:
#     if i not in setNums:
#         setNums.append(i)
#     else:    
#         k = i
#         while k in setNums:
#             m += 1
#             k += 1
#         setNums.append(k)
# # print(m)

q = []
l = 0
for i in nums:
    if i not in q:
        q.append(i)
    else:
        mx = max(q)+1
        if mx not in q:
            l += (mx-i)
            q.append(mx)
print(q, l)

class Solution:
    def minIncrementForUnique(self, nums) -> int:
        min_increments = 0

        nums.sort()

        for i in range(1, len(nums)):
            # Ensure each element is greater than its previous
            if nums[i] <= nums[i - 1]:
                # Add the required increment to minIncrements
                increment = nums[i - 1] + 1 - nums[i]
                min_increments += increment

                # Set the element to be greater than its previous
                nums[i] = nums[i - 1] + 1

        return min_increments