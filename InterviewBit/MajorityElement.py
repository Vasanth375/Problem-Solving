# Accepted 

from math import floor
a = [2,1,2,2]
#a = [1,1,2]
#a = [100]

if len(a) == 1:
    print(a)

timesAppear = floor(len(a)//2)

dictElement = {}

for i in a:
    dictElement[i] = a.count(i)
    if a.count(i) > timesAppear:
        print(i)
        break
