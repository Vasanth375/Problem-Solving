a = "xy"
# a = 'yy'
count = 0
i = 0
while i < len(a)-1:
    ## if we find any pair like xy or yx then
    # counter incremented by 1 and i incremented by 2 that means
    # we found a pair so don't include the involed xy in any other pairs
    if a[i] != a[i+1]:
        count += 1
        i += 2
    else:
        i += 1
print(count)