arr=[1,2,3,4,5]
tempar=[]
n=0
in1=5
in2=4
size=len(arr)
# for i in range(len(arr)):
#     if(arr[i]==in1 or arr[i]==in2):
#         tempar.append(arr[i])
# print(tempar)
for i in range(size):
    if(in1!=arr[0]):#5!=
        n=arr[i]
        #arr.remove(arr[i])
        arr[size]=n
print(arr)
