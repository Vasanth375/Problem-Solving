boxes = "110"
boxes = "001011"
n = len(boxes)
k = []
for indexi in range(len(boxes)):
    count = 0
    for indexj in range(len(boxes)):
        if boxes[indexj] == '1' and indexi != indexj:
            count += abs(indexi-indexj)
    k.append(count)
print(k)
