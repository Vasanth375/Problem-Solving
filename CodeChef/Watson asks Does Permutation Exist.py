# Brute Force
n = 4
a = [3,2,2,3]

# n = 2
# a = [1,5]
## first we should sort the list
a.sort()
flag = True

## iterate over the list 
# check the condition if i+1 - i > 1 or not 
# if adjacent pairs subtraction gives more than 1 print it as NO(can't reorganized)
for i in range(0,len(a) - 1):
    if (a[i+1] - a[i]) > 1:
        flag = False
        break

if flag:
    print("YES")
else:
    print("NO")