# Accepted
bill = [3, 10, 2,9]
k = 1
b = 12

sum1 = 0
bill.remove(bill[k])
sum1 = sum(bill)
actual = sum1//2
if actual != b:
    print(b - actual)
else:
    print("Bon Appetit")
