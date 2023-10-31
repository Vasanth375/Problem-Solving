pref = [5,2,0,3,1]
# pref = [13]
# pref = [413935,351122]

arr = [pref[0]]

i = 1
while i < len(pref):
    arr.append(pref[i]^pref[i-1])
    i += 1
print(arr)