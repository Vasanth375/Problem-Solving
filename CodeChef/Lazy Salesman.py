w = 10
a = [3, 2, 6, 1, 3]

w, a = 15, [3, 2, 4, 6]

w, a = 8, [9, 12, 6, 5, 2, 2]

sortedA = sorted(a, reverse=True)

count = 0

s = 0
for i in sortedA:
    s += i
    if s >= w:
        print(len(a) - sortedA.index(i) - 1)
        break
