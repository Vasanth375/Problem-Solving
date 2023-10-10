# Hard Problem

class Solution:
    def mySolution(self, nums):
        return min(nums)

    def findMin(self, nums):
        if not nums: return 5001
        if len(nums) == 1: return nums[0]

        # use a binary search to try to find an inflection point
        low = 0
        high = len(nums)-1
        while low <= high:
            if nums[high] > nums[low]:
                return nums[low]     # if sorted, then min is at low  
            mid = low + (high - low) // 2

            if nums[mid-1] > nums[mid]:
                return nums[mid]    # if inflection point(point which divides the array) is found
            
            # below code is equivalent to the above code
            # if nums[mid] < nums[mid+1]:
            #     return nums[mid]

            # if the right side is sorted, then inflection on left
            if nums[high] > nums[mid]:    
                high = mid-1
            # if the left side sorted, then inflection on right (also check that right side is not flat)
            elif nums[low] < nums[mid]:     
                low = mid+1
            # case where both are the same; not enough info; evaluate both sides    
            else:                           
                return min(self.findMin(nums[low:mid]), self.findMin(nums[mid+1:high+1])) # type: ignore

sol = Solution()
print(sol.findMin([2,2,2,0,1]))
print(sol.findMin([]))