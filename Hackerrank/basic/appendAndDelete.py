def appendAndDelete(s, t, k):
    i = 0

    # finding the same elements from the both lists and counting them
    while i < min(len(s), len(t)) and s[i] == t[i]:
        i += 1
        
    # find the minimum moves from the counted i
    min_moves = (len(s) - i) + (len(t) - i)

    #finding the max moves by adding both values
    max_moves = len(s) + len(t)

    if k < min_moves:
        return('No')
    elif k == min_moves or k >= max_moves:
        return('Yes')
    elif (k - min_moves) % 2 == 0:
        return('Yes')
        
    return('No')


s = ['a','a','a','a','a','a','a', 'a','a','a']
t = ['a','a','a','a','a']
k=7
print(appendAndDelete(s,t,k))
