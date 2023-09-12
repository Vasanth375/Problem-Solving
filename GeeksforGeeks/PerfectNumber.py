n=2
import math
k = []
if n==0 or n==1:
    print(0)

# this piece of code is the optimized version
# to find factors of a number in O(sqrt(n)) complexity

# Note that this loop runs till square root
i = 1
while i <= math.sqrt(n):
        
    if (n % i == 0) :
            
        # If divisors are equal, print only one
        if (n / i == i) :
            # print (i,end=" ")
            pass
        else :
            # Otherwise print both
            # print (i , int(n/i), end=" ")
            k.append(i)
            k.append(int(n/i))
    i = i + 1
k.remove(n)

if sum(k) == n:
    print(1)
else:
    print(0)