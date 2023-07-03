nums = [1, 5, 0, 3, 5]

# Solved Using resursion approach
class Solution:
    def repeatStep(self, nums, count):
        # k = [i for i in nums if i != 0]
        k = nums.copy()
        for i in range(k.count(0)):
            k.remove(0)

        if len(k) == 0:
            return count

        count += 1
        
        minNum = min(k)
        m = []
        for i in nums:
            if (i - minNum) >= 0:
                m.append((i - minNum))
            else:
                m.append(0)
        return self.repeatStep(m, count)

    
    def minimumOperations(self, nums) -> int:
        count = 0
        return self.repeatStep(nums, count)