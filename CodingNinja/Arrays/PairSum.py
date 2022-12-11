# ACCEPTED
def PairSum(arr, n):
    l = []
    arr = sorted(arr)
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if (arr[i] + arr[j]) == n:
                l.append(tuple(sorted([arr[i], arr[j]])))
    print(l)


PairSum([1,2,3,4,5], 5)
#PairSum([2,-3,3,3,-2], 0)
