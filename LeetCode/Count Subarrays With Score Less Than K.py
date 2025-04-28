def countSubarrays(nums, k):
    n = len(nums)
    count = 0
    curr_sum = 0
    start = 0
    
    for end in range(n):
        curr_sum += nums[end]
        curr_len = end - start + 1
        
        # While the score is >= k, shrink the window
        while start <= end and (curr_sum * curr_len) >= k:
            curr_sum -= nums[start]
            start += 1
            curr_len = end - start + 1
            
        # Add all possible subarrays ending at 'end'
        if start <= end:
            count += end - start + 1
            
    return count

# Test cases
nums = [2,1,4,3,5]
k = 10
print(countSubarrays(nums, k))  # Expected output: 6

nums = [1,1,1]
k = 5
print(countSubarrays(nums, k))  # Expected output: 5
