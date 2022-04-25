k=4
a=[1 ,6 ,3 ,5 ,2]

def hurdle_race(k, height):
    n = max(height) - k
    if n>0:
        return n
    return 0

print(hurdle_race(k, a))