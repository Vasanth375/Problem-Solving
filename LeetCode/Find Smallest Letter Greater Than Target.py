letters = ["c","f","j"]
target = "a"

letters = ["c","f","j"]
target = "c"

letters = ["x","x","y","y"]
target = "z"

letters.append(target)
letters = list(set(letters))
letters.sort()
if target == letters[-1]:
    print(letters[0])
else:
    k = letters.index(target)
    print(letters[k+1])