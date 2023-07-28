a, b = 123, 234
digits = {
    0: 6,
    1: 2,
    2: 5,
    3: 5,
    4: 4,
    5: 5,
    6: 6,
    7: 3,
    8: 7,
    9: 6,
}

sumab = str(a+b)

sumab = [int(i) for i in sumab]

sumDigits = [digits[i] for i in sumab]
print(sum(sumDigits))