from math import comb
from collections import Counter

'''
Background Knowledge:
combination function is used to find the number of ways to find the k occurences of n valueThe combination function, 
also known as the binomial coefficient or 'n choose k,' is a mathematical operation that calculates the number of distinct 
combinations of 'k' elements that can be selected from a set of 'n' elements, without regard to their order.
math.comb(5, 2)
here we are finding the number of ways to choose 2 elements from a set of elements 5
formula - n!/k!*(n-k)!
-----
nCk = comb(5, 2)
'''

l = [1, 5, 5, 5, 9, 9, 9]

# this will return a dictionary containing the number with their number of occurrences of each element
sl = Counter(l)

count = 0
for i in sl:
    # here it just returns the number of ways to partition the sl[i] element with 2 occurrences
    # if sl[i] value less than 2 then returns 0
    count += comb(sl[i], 2)
print(count)

