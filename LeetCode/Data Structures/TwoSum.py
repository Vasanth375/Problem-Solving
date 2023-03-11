class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        checked = {}
        i = 0

        # checking is target - nums[i] not in dictionary
        while target - nums[i] not in checked:

            # if not exist add it to the dict
            checked[nums[i]] = i
            i += 1
        print(checked)
        # finally from dictionary find the target - 
        return [checked[target - nums[i]], i]


s = Solution()
nums = [2,7,11,15]
target = 9
print(s.twoSum(nums, target))
