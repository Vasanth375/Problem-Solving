arr = [1,2,3,4,5]
k = 4
x = 3

arr = [1,1,2,3,4,5]
k = 4
x = -1

# arr = [0,0,1,2,3,3,4,7,7,8]
# k = 3
# x = 5

# O(N log N)

distance_dict = {}
for num in arr:
    dist = abs(num - x)
    if dist not in distance_dict:
        distance_dict[dist] = []
    distance_dict[dist].append(num)

result = []
for dist in sorted(distance_dict.keys()):
    for num in sorted(distance_dict[dist]):
        result.append(num)
        if len(result) == k:
            break
    if len(result) == k:
        break
result.sort()
print(result)

