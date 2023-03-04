class Solution:
    # @param A : integer
    # @return a list of integers
    def getRow(self, N):
        prev = 1
        l = []
        l.append(prev)
        #print(prev, end = '')
        for i in range(1, N + 1):
            # nCr = (nCr-1 * (n - r + 1))/r
            curr = (prev * (N - i + 1)) // i
            l.append(curr)
            prev = curr
        return l

s = Solution()
print(s.getRow(4))