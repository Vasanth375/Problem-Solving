
class Solution:
    def __init__(self) -> None:
        self.pick = 4

    def guess(self, n):
        if n == self.pick:
            return 0
        if n > self.pick:
            return -1
        if n < self.pick:
            return 1
    def guessNumber(self, n: int):
        low = 0
        high = n
        while low <= high:
            mid = (low+high)//2

            if self.guess(mid) == -1:
                high = mid-1
            elif self.guess(mid) == 1:
                low = mid+1
            else:
                return mid
sol = Solution()
print(sol.guessNumber(4))