from collections import Counter

a = [5, 5, 1, 5, 1, 5]
# a = [4, 4, 4]
# a = [1, 2, 2, 3]
# a = [2, 3, 3, 2]

s = set(a)
## here we are using the counte to find the number of occurrences
# of each number 
flag = 0
for i in s:
    ## if number of occurrences is even then flag is set to 1
    # becouse list is equally distributed to Alice and Bob
    if a.count(i) % 2 == 0:
        flag = 1
    else:
        flag = 0
        break

if flag == 1:
    print("YES")
else:
    print("NO")
