derived = [1,1,0]

# Edge cases
# if len(derived) == 1 and derived[0] == 0:
#     return True

# if len(derived) == 1 and derived[0] == 1:
#     return False

original = []
flag = True
for i in range(len(derived)):
    
    if i == len(derived)-1:
        if original[i]^original[0] == derived[i]:
            flag = True
        else:
            flag = False
    elif i == 0:
        if 0 ^ 1 == derived[i]:
            original.append(0)
            original.append(1)
        elif 1 ^ 0 == derived[i]:
            original.append(1)
            original.append(0)
        elif 0 ^ 0 == derived[i]:
            original.append(0)
            original.append(0)
        else:
            flag = False
    else:
        if original[i]^0 == derived[i]:
            original.append(0)
        elif original[i] ^ 1 == derived[i]:
            original.append(1)
        else:
            flag = False
        
print(flag)
