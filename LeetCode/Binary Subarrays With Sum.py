'''
Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.

A subarray is a contiguous part of the array.
'''

nums = [0,0,0,0,0]
goal = 0
# Sliding Window approach
# Below Algorithm is used to find number of subarrays lessthan or equal to the goal and
# less than or equal to goal-1 then we get exact subarrays of equal to goal value
def help(goal):    
    l = 0
    r = 0

    sum1 = 0
    count = 0
    if goal < 0:
        return (0)
    while r <= len(nums)-1:
        sum1 += nums[r]
        
        # if sum > goal removing from left side 
        while sum1 > goal:
            sum1= sum1 - nums[l]
            l += 1
        
        # adding position
        count = count + (r-l+1)
        r += 1
    return (count)

print(help(goal) - help(goal-1))