sentence = "thequickbrownfoxjumpsoverthelazydog"

a = "abcdefghijklmnopqrstuvwxyz"
k = 0
for i in a:
    if sentence.count(i) >= 1:
        k += 1
    elif sentence.count(i) == 0:
        print(False)
        break
print(k)
