a = "   fly me   to   the moon  "
a="    day"

a = a.strip()
if len(a) == 1:
    print(1)

l = list(a)

f = ""
for i in range(1,len(l)+1):
    if l[-i] == " ":
        break
    else:
        f+=l[-i]
f = list(f)
f.reverse()
print(len(f))