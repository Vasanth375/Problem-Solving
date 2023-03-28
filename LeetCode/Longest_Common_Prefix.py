str = ["flower","flow","flight"]

a = ""

# sort the list
str.sort()

# now just compare first and last strings
m = str[0]
n = str[-1]

# perform the loop by minimum length
length = min(len(m), len(n))


for i in range(length):
    if m[i] != n[i]:
        break
    else:
        a+=m[i]

if a != "":
    print(a)
else:
    print("")

