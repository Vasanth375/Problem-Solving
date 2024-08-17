# Time Complexity
# O(N * M)
def lists_equal(word, patt):
    d = {}
    if len(set(word)) != len(set(patt)):
        return False
    newstr = ""
    for i in range(len(word)):
        if word[i] not in d.keys():
            d[word[i]] = patt[i]
        elif word[i] in d.keys():
            if d[word[i]] != patt[i]:
                return False
            
    print(newstr)
    return True

words = ["abc","deq","mee","aqq","dkd","ccc"]
pattern = "abb"

words = ["badc","abab","dddd","dede","yyxx"]
pattern = "baba"

res = []
for string in words:
    if lists_equal(string, pattern):
        res.append(string)
print(res)