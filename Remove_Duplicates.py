s="pwwkewpu"
temp,l=[],""
for index,value in enumerate(s):
    if value not in temp:
        temp.append(value)

print(temp)
print(len(temp))
