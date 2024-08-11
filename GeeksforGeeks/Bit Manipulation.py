# n = 446733544 
# i = 30

n = 70
i = 3

# n = 224433946
# i = 31

i=i-1
getBit=1 if n & (1<<i) else 0
setBit=n | (1<<i)
clrBit= n & ~(1<<i)
print(getBit,setBit,clrBit,end="")
