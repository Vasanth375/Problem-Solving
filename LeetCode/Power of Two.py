## this problem has special mathematical view among other problems
## all 1,2,4,8,... in binary form it's MSB is 1 so here's the observation we have to note
## please refer to the Link to see more details\
# https://leetcode.com/problems/power-of-two/solutions/1638707/python-c-java-detailly-explain-why-n-n-1-works-1-line-100-faster-easy/

def isPowerOfTwo(self, n):
    return n and not (n & n - 1)
