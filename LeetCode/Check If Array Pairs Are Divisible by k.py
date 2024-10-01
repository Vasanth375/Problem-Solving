arr = [1,2,3,4,5,10,6,7,8,9]
k = 5

arr = [1,2,3,4,5,6]
k = 10
# My Approach sorting and Two POinters

# arr = [1,2,3,4,5,6]
# k = 7
# arr = [3,8,7,2]
# k = 10

# i = 0
# j = 1
# count = 0
# while j < len(arr):
#     if (arr[i] + arr[j]) % k == 0:
#         count += 1
#         i += 1
#         j += 1
#     else:
#         j += 1

# Same approach but slightly different implementation
arr = sorted(arr, key=lambda x: (k + x % k) % k)

# Assign the pairs with modulo 0 first.
start = 0
end = len(arr) - 1
while start < end:
    if arr[start] % k != 0:
        break
    if arr[start + 1] % k != 0:
        print("False")
    start = start + 2

# Now, pick one element from the beginning and one element from the
# end.
while start < end:
    if (arr[start] + arr[end]) % k != 0:
        print("False")
    start += 1
    end -= 1

print("True")