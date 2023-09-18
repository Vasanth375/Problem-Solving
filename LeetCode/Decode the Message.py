key = "the quick brown fox jumps over the lazy dog"
message = "vkbs bs t suepuv"

# key = "eljuxhpwnyrdgtqkviszcfmabo"
# message = "zwx hnfx lqantp mnoeius ycgk vcnjrdb"

alpha = "abcdefghijklmnopqrstuvwxyz"


setKey = ""
for i in key:
    if i not in setKey and i != " ":
        setKey += i
print(setKey, len(setKey))

message = message.split(" ")
dic = ""

for string in message:
    for i in string:
        k = setKey.find(i)
        dic += alpha[k]
    dic += " "

print(dic[:len(dic)-1])