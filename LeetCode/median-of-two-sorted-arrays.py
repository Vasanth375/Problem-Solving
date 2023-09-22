# Leetcode - Hard problem
# solved 

num1 = [1,2]
num2 = [3,4]

med = num1+num2

med.sort()

mid = len(med)//2
if len(med) % 2!=0:
    print(med[mid])
else:
    add = med[mid-1]+ med[mid]
    print(add/2)
