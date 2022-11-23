'''
Given an array and value d 

check the increasing values(values not index) with array value that is equal to d then increament count to count beautiful triplet
'''

d = 3
arr = [1,2,4,5,7,8,10]
arr= [2,2,3,4,5]
d= 1
count = 0
for i in arr:
    if (i + d in arr) and(i + 2*d in arr):  # iterating each value from arr and adding it with the d and 2*d value and
        count += 1                          # same time checking the computed values are there in arr or not
print(count)