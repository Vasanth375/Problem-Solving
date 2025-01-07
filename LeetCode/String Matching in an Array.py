words = ["mass","as","hero","superhero"]
words = ["leetcode","et","code"]
words = ["blue","green","bu"]

newWords = []
indexs = []
for indexi in range(len(words)):
    for indexj in range(len(words)):
        if indexi != indexj:
            if words[indexi] in words[indexj] and indexi not in indexs:
                newWords.append(words[indexi])
                indexs.append(indexi)
                break
            elif words[indexj] in words[indexi] and indexj not in indexs:
                newWords.append(words[indexj])
                indexs.append(indexj)
                break

print(newWords)