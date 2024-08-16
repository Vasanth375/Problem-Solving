arr = [90, 15, 10, 7, 12, 2]
arr += [-1]*(len(arr)+1)
flag = 0
for i in range(len(arr)):
    key = arr[i]
    if key == -1:
        break
    if key >= arr[(i*2)+1] and key>=arr[(i*2)+2]:
        flag = 1
    else:
        flag = 0
        break
    # print(arr[(i*2)+1])
print(flag)

#print(arr[2*2+2])
