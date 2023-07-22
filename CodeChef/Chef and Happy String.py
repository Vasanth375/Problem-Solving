arr = "aebcdefghij"
arr = "abcdeeafg"
count = 0

for i in arr:
    if i in "aeiou":
        count += 1
        if count > 2:
            print("happy")
    else:
        count = 0