import heapq

a = 7
b = 1
c = 1
res = ""
maxHeap = []
for count, char in [(-a, "a"), (-b, "b"), (-c, "c")]:
    if count != 0:
        heapq.heappush(maxHeap, (count, char))

while maxHeap:
    count, char = heapq.heappop(maxHeap)

    # checking if consecutive 3 chars exist in result 
    if len(res) > 1 and res[-1] == res[-2] == char:

        # if maxheap is empty
        if not maxHeap:
            break

        # if the condition breaks adding another value to the result 
        count2, char2 = heapq.heappop(maxHeap)

        res += char2
        count2 += 1
        # if count is not empty
        if count2:
            heapq.heappush(maxHeap, (count2, char2))
    else:
        # if there are different values in the result
        res += char
        count += 1
    if count:
        heapq.heappush(maxHeap, (count, char))
print(res)
