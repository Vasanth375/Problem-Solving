l = [1, 30, 30]
a = [2, 1, 3]
n =3
c = 0
for j in range(n):
    gc = 0
    lc = 0

    ## here this will check from 0 to j-1 index 
    for k in range(j):
        # comparing j to k index
        if a[j] < a[k]:
            gc = gc + 1
            # print("1 gc ",gc)
        else:
            lc = lc + 1
            # print("2 lc",lc)
    ## here this loop will check from j+1 to n 
    for l in range(j + 1, n):
        if a[j] < a[l]:
            gc = gc + 1 
            # print("3 gc",gc)
        else:
            lc = lc + 1
            # print("4 lc",lc)
    # now checking that greater common and lowest common, increment counter
    if gc <= lc:
        c = c + 1
print(c)
