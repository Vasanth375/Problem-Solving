s = "leet**cod*e"
#s = "erase*****"

a = []

for i in s:
    a.append(i)
    # pop the two values from the top of list if the condition true
    if i == "*":
        a.pop()
        a.pop()


print("".join(a))