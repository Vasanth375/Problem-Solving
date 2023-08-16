s = 'chef'

s = 'sharechat'
alpha = "abcdefghijklmnopqrstuvwxyz"

k = ''
n = len(s)

for i in range(0, n-1, 2):
    k += s[i+1] + s[i]

if n%2 == 1:
    k += s[n-1]

encode = ""
for i in k:
    f = alpha.index(i)+1
    encode += alpha[-f]
print(encode)