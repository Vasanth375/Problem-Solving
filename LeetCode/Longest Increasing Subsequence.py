nums = [10, 9, 2, 5, 3, 7, 101, 18]
# nums = [0,1,0,3,2,3]
# nums = [7,7,7,7,7,7,7]
# nums = [4,10,4,3,8,9]
'''
Approach
We can initialize an array dp of the same length as the input array nums, where dp[i] represents the length of the
longest increasing subsequence ending at index i. We can iterate through the array and update dp based on the elements 
before the current index. The final result will be the maximum value in the dp array.
'''

if not nums:
    print(0)

n = len(nums)
dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if nums[i] > nums[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
