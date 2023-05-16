n = 7
c = 0

## here we are finding the number of nodes in the tree while
##  h*(h+1)/2 is used to find the number of nodes in the tree
for i in range(1, n + 1):
    i = i * (i + 1) / 2

    # each time we should check the number of nodes with coins we have so that 
    if i > n:
        break
    else:
        c += 1
print(c)
