a = 20
b = 23
k = 6


def reversedNumber(number):
    temp = str(number)
    temp = [i for i in temp]
    temp.reverse()
    return int("".join(temp))

count = 0
for i in range(a, b + 1):
    num = reversedNumber(i)
    temp = abs(i - num) / k
    if temp.is_integer():
        count += 1

print(count)

# -----------------------------------
# Sample example of how an is_integer function works
# a = 7
# b = 2

# result = a / b

# if result.is_integer():
#     print(int(result))
# else:
#     print(result)
