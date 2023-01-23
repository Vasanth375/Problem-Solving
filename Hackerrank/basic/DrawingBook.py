#n - number of pages in book
#p - page number to turn to
n = 5
p = 3

# n = 6
# p = 2

# n = 5
# p = 4
k =0
count = 0
q = []
for i in range(0,n+1):
    k+=1
    if p == i:
        q.append(count)
        break
    if k == 2:
        count+=1
        k = 0

k = 0
count = 0
for i in reversed(range(0, n+1)):
    k+=1
    if p == i:
        q.append(count)
        break
    if k == 2:
        count+=1
        k = 0
print(min(q))