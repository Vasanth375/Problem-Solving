# Accepted

s = "abacaba"
s = "ssssss"
k = []
l = []

# iterate and append it to k list
for i in s:

    # storing only unique values in k list
    if i not in k:
        k.append(i)
    # this block reach if we try to insert duplicate value
    else:
        l.append(k)
        k = []
        k.append(i)

# 
print(len(l)+1)
