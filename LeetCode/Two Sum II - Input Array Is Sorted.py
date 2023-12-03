numbers = [2, 7, 11, 15]
target = 9

numbers = [2, 3, 4]
target = 6

numbers = [0, 0, 3, 4]
target = 0

numbers = [5, 5, 5, 25, 25, 75, 80, 85, 90]
target = 100

numbers = [0, 0, 3, 4]
target = 0


k = []
m = []
for i in range(len(numbers)):
    # here we are just checking unique values only
    if numbers[i] not in m:
        m.append(numbers[i])
        for j in range(i+1, len(numbers)):
            if (numbers[i] + numbers[j]) == target:
                k = [i+1, j+1]
                break
        if k:
            break
print(k)

# Runtime - 104ms
# Memory - 17MB
