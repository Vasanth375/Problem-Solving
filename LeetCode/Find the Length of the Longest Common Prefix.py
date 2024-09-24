
# def check(a,b, n:list):
#     a = str(a)
#     b = str(b)
#     q = ""

#     for m in range(min(len(a), len(b))):
#         if a[m] == b[m]:
#             q += a[m]
#         else:
#             break
#     if len(q) > len(n[0]):
#         n[0] = q



# arr1 = [1,10,100]
# arr2 = [1000]

# # arr1 = [10]
# # arr2 = [17, 11]


# i = 0
# n = [""]
# while i < len(arr1):
#     k = arr1[i]
#     for j in arr2:
#         check(k, j, n)
#     i += 1
# print(n)

# if n[0] == "":
#     print(0)
# print(n[0])

arr1 = [1,10,100]
arr2 = [1000]

arr1_prefixes = set()  # Set to store all prefixes from arr1

# Step 1: Build all possible prefixes from arr1
for val in arr1:
    while val not in arr1_prefixes and val > 0:
        # Insert current value as a prefix
        arr1_prefixes.add(val)
        # Generate the next shorter prefix by removing the last digit
        val //= 10

longest_prefix = 0

# Step 2: Check each number in arr2 for the longest matching prefix
for val in arr2:
    while val not in arr1_prefixes and val > 0:
        # Reduce val by removing the last digit if not found in the prefix set
        val //= 10
    if val > 0:
        # Length of the matched prefix using log10 to determine the number of digits
        longest_prefix = max(longest_prefix, len(str(val)))
