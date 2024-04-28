'''Given an array of integers, find the longest subarray where the absolute difference between 
any two elements is less than or equal to .'''

a = [4, 6, 5, 3, 3, 1]
# using hashmap to count the number of times a value repeated
hash_map = {}
max_len = 0
for i in a:
    if i in hash_map:
        hash_map[i] += 1
    else:
        hash_map[i] = 1
    # if i = 3 we checking 2 and 4 value also where the difference between 3-2 or 3-4 or vice-versa
    # difference is <= 1 condition satisfied
    # so by adding the count value of each number and finding the max value
    # before the number
    if (i - 1) in hash_map:
        max_len = max(max_len, hash_map[i] + hash_map[i - 1])
    # after the number
    if (i + 1) in hash_map:
        max_len = max(max_len, hash_map[i] + hash_map[i + 1])
    # the exact number
    max_len = max(max_len, hash_map[i])
print(max_len)