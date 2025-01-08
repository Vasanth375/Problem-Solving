words = ["pa","papa","ma","mama"]
#words = ["a","aba","ababa","aa"]

def isPrefixAndSuffix(a, b):    
    al = len(a)

    # prefix 
    # print(b[:al])
    # print(b[-al:])
    if a == b[:al] and a == b[-al:]:
        return (True)

count =0
for i in range(len(words)):
    for j in range(i+1, len(words)):
        if isPrefixAndSuffix(words[i], words[j]):
            count += 1
print(count)