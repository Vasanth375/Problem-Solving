# reversing the string
s = "This is an Intro"
s = list(map(str,s.split()))
s.reverse()
for i in s:
    print(i, end=" ")