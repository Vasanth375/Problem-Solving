# Time Complexity
# O(N * M)
def lists_equal(word, patt):
    d = {}
    
    # basecase - if length of unique string is different return False
    if len(set(word)) != len(set(patt)):
        return False
    
    for i in range(len(word)):
        # Checking whether the character is mapped or not
        if word[i] not in d.keys():
            d[word[i]] = patt[i]
        elif word[i] in d.keys():
            # if already mapped then checking whether the mapped value and pattern character equal or not
            if d[word[i]] != patt[i]:
                print(word)
                return False

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