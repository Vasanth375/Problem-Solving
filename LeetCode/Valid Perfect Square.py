n = 104976
flag = False

# using Binary Search Approach - 
if n <= 1:
    print(True)

left, right = 1, n
while left <= right:
    mid = left + (right - left)//2
    square = mid * mid
    if square == n:
        flag = True
        break
    # if square is smaller than n, search the square in right half
    if square < n:
        left = mid + 1
    # if square is greater than n, search the square is left half
    elif square > n:
        right = mid - 1

print(flag)