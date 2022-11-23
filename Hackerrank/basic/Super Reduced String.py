import functools

def reduce_string(s,c):
    if s and s[-1] == c:
        return s[:-1]
    else:
        return s+c

# reduce function will return a value from set of values by performing an operation 
res = functools.reduce(reduce_string, "aabbcddd")
if res:
    print(res)
else:
    print("Empty String")
