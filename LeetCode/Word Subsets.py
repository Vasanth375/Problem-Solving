from collections import Counter, defaultdict

words1 = ["amazon","apple","facebook","google","leetcode"]
words2 = ["e","o"]

words1 = ["amazon","apple","facebook","google","leetcode"]
words2 = ["l","e"]

words1  = ["acaac","cccbb","aacbb","caacc","bcbbb"]
words2 = ["c","cc","b"]

words1 = ["amazon","apple","facebook","google","leetcode"]
words2 = ["lo","eo"]

k = defaultdict(int)
for i in words2:
    count2 = Counter(i)
    for j,v in count2.items():
        # k[j] = k.get(i.count(j),0)
        k[j] = max(k[j], v)
print(k)

res = []
for word in words1:
    eachword = Counter(word)
    flag = True
    for key, value in k.items():
        if eachword[key] < value:
            flag = False
            break
    if flag:
        res.append(word)
print(res)
