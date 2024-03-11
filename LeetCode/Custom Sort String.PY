order = "cba"
s = "abcd"
order = "bcafg"
s = "abcd"

order = "kqep"
s = "pekeq"

order = "hucw"
s = "utzoampdgkalexslxoqfkdjoczajxtuhqyxvlfatmptqdsochtdzgypsfkgqwbgqbcamdqnqztaqhqanirikahtmalzqjjxtqfnh"

k = ""
last = ""
taken = ""

for i in order:
    if i in s and i not in taken:
        l = s.count(i)
        k += i * l
        taken += i
    else:
        if i not in taken:
            last += i * s.count(i)
            taken += i

for i in s:
    if i not in k and i not in taken:
        last += i * s.count(i)
        taken += i
last = list(last)
last.sort()
print(k+"".join(last))
