'''
Approach: Math
Intuition
In this problem, we have some dice throw results but lost n of them. We know the results of m throws and
the average value of all m + n throws. Our goal is to determine if we can find the missing throws that fit these conditions.

The mean is the sum of observations divided by the number of observations. Therefore, we can find the total sum by 
multiplying the mean by m + n. Next, we subtract the sum of the m known throws from this total sum to get the sum of the missing n throws.

For example:
rolls=[3,2,4,3],mean=4,n=2
totalobservations=m+n=4+2=6
sumofobservations=4∗6=24
sumofgivendicerolls=6∗2=12
sumofremainingdicerolls=24−12=12

To check if this sum is possible, we note that the minimum sum for n dice is n (if all dice show 1), and the maximum 
sum is 6n (if all dice show 6). So, the sum of the missing throws must be between n and 6n, inclusive.

Finally, we need to distribute this sum among the n missing throws. Ideally, each missing throw would have a value 
close to the average. If the sum isn’t exactly divisible by n, we distribute the remainder among the throws, making sure 
each value stays between 1 and 6.
'''


rolls = [3,2,4,3]
mean = 4
n = 2

rolls = [1,5,6]
mean = 3
n = 4

sum1 = 0
sum1 = sum(rolls)

remainsum = mean * (n + len(rolls)) - sum1

if remainsum > 6*n or remainsum < n:
    print([])

distrbuteMean = remainsum//n 
mod = remainsum&n

nElements = [distrbuteMean]*n
for i in range(mod):
    nElements[i] += 1
print(nElements)