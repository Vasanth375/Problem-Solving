# ACCEPTED
s1 = 'hi'
s2 = 'world'

# First set returns the unique and unordered set from the strings
strings1 = set([*s1])
strings2 = set([*s2])

# simply intersection means common in both sets
intersectedStrings = strings1.intersection(strings2)

# If we have comman it will returns the new set or its empty
if len(intersectedStrings) > 0:
    print("YES")
print("NO")


# check = False
# for i in a:
#     if i in b:
#         check = True
#         break

# if check:print('Yes')
# else:print('No')