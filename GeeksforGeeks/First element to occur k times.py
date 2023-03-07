def ktimes(a,k):
    res=[0]*10000
    # here we have length of the array is 10^4 so we have to create 10^4 (10000) size of array and
    # what ever the element that meets the condition we have to print it first
    for i in a:
        res[i]+=1
        if res[i]==k:
            return i
    else:
        return -1

print(ktimes([1,7,4,3,5,7,4, 7], 2))
