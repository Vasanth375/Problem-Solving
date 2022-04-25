s="hhaacckkekraraannk"
n=0
a,i,temp="hackerrank",0,0

# Checking if hackerrank string is there in s variable or not
for j in range(len(s)):
    if a[i] == s[j]:
        n+=1;i=i+1
        if n == len(a): # Checking n and length of a
            temp=1
            break # break if a is found in s
if temp == 1:
    print('YES')
else:
    print('NO')
