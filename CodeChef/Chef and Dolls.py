# returing the missing doll from the collection which will come exactly once

k = [1, 2, 1, 3]

m = 0
for i in k:
    '''printing the i value when odd number of elements in the collection '''
    if k.count(i) % 2 == 1:
        m = i
        break
print(m)
