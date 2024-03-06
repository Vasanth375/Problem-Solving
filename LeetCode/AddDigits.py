def convertStringTo(number):
    Lnum = str(num)
    Lnum = [int(x) for x in Lnum]
    return Lnum


num = 0

while True:
    lnum = convertStringTo(num)
    if len(lnum) == 1:
        print(sum(lnum))
        break
    num = sum(lnum)

