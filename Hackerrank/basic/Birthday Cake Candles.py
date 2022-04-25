candles=[1,2,3,1,3]
ed=sorted(candles)
n=ed[len(ed)-1]
k=0
for i in candles:
    if n==i:
        k=k+1
print(k)