#
# Given an array of integers nums and an integer k, return the number of contiguous
# subarrays where the product of all the elements in the subarray is strictly less than k.
#

nums = [10, 5, 2, 6]
k = 100

total = 0
running = 1
left = 0
# USING SLIDING WINDOW
for right in range(len(nums)):
    # calculating product of current right value
    running *= nums[right]

    #sliding to the right side and removing the left value from the subarray product
    while left < right and running >= k:
        running //= nums[left]
        left += 1

    # our case is if product less than k then count the subarray
    if running < k:
        total += right - left + 1
print(total)
