word = "zjpc"
word = "bza"
word = "abc"

count = 0
start = 'a'
for i in word:
    count += min(abs(ord(i) - ord(start)), 26 - abs(ord(i) - ord(start)))
    start = i
print(count + len(word))

