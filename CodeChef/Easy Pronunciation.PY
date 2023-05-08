s = "apple"
s = "schtschurowskia"
# s = "polish"
# s = "tryst"
# s = "cry"
n = len(s)
if(n<=3):
    print("YES")
else:
    for i in range(n-3):
        s1=s[i:i+4]
        x='a' in s1 or 'e' in s1 or 'i' in s1
        y='o' in s1 or 'u' in s1
        if not x and not y:
            print('NO')
            break
    else:
        print('YES')    