# Not Optimized
n = 4
x = 3
a = [1,5,9,23]
# a = [1,1,1]
a.sort()
k = -1
for i in range(n):
    m =  bin(a[i])
    if len(m) >= x:
        for j in range(i+1, n):
            y = bin(a[j])
            if (m[-x] =='0' and y[-x] == '1') or (m[-x] =='1' and y[-x] == '0'):
                if a[i] + a[j] > k:
                    k = a[i] + a[j]
print(k)

k = -1
# Assuming a is a list of integers, and n is its length
# x is the bit position (1-based) to compare
a.sort()
k = -1
for i in range(n):
    for j in range(i + 1, n):
        # Compare the bits at the (x-1)th position (0-indexed)
        bit_i = (a[i] >> (x - 1)) & 1
        bit_j = (a[j] >> (x - 1)) & 1

        # Check if the bits are different
        if bit_i != bit_j:
            k = max(k, a[i] + a[j])
        else:
            break  # Break if bits are the same, as sorted array means no more useful pairs
print(k)