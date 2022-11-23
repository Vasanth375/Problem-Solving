
from itertools import groupby

S = input()
# S = [int(i) for i in "1222311"]
set_S = list(set([int(i) for i in S]))

consecutive = []

# research this constructor and write it's context here
S = groupby(S)
for i, v in S:
    consecutive.append(tuple([len(list(v)), i]))
for i in consecutive:
    print(i, end=" ")
