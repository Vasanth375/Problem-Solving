## ACCEPTED

word1 = "abc"
word2 = "pqr"
word1 = "ab"
word2 = "pqrs"
word1 = "abcd"
word2 = "pq"
# w1 = list(" ".join(word1))
# w2 = list(" "+" ".join(word2))
l = []
if len(word1) == len(word2):
    for i,j in zip(word1, word2):
        l.append(i)
        l.append(j)
    print(l)
elif len(word1) < len(word2):
    for i in range(len(word1)):
        l.append(word1[i])
        l.append(word2[i])
    l.extend(word2[len(word1):])
    print(l)
else:
    for i in range(len(word2)):
        l.append(word1[i])
        l.append(word2[i])
    l.extend(word1[len(word2):])
    print(l)

#------------------------------------------
# simple approach with 15ms
answer = ""

for i in range(min(len(word1), len(word2))):
    answer = answer + word1[i] + word2[i]
print(answer + word1[min(len(word1), len(word2)):] + word2[min(len(word1), len(word2)):])