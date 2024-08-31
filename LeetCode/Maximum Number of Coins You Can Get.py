piles = [2,4,1,2,7,8]
piles = [2,4,5]
piles = [9,8,7,6,5,1,2,3,4]

piles.sort()
me = 0
i = 0   # points to min
j = len(piles)-1    # points to max
while i < j:
    j-=1 # alice
    me += piles[j]
    j-=1 # me
    i+=1 # bob
print(me)