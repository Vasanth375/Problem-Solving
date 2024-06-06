# concepts used - heapq, priority queue, hashtable

from collections import Counter
import heapq


hand =[1,2,3,6,2,3,4,7,8]
groupSize = 3

# hand = [1,2,3,4,5]
# groupSize = 4
# hand = [2,1]
# groupSize = 2

def handL(hand, groupSize):
    k = Counter(hand)
    minh = list(k.keys())
    heapq.heapify(minh)
    while minh:
        fir=minh[0]
        for i in range(fir, fir+groupSize):
            if i not in k:
                return (False)
            
            k[i] -= 1
            if k[i] == 0:
                if i != minh[0]:
                    return (False)
                heapq.heappop(minh)
    return (True)

print(handL(hand, groupSize))