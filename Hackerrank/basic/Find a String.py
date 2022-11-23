# find a string
string = "ABCDCDC"
k = "CDC"
count = 0

for i in range(len(string)):
    if string[i:].startswith(k):
        count+=1
print(count)