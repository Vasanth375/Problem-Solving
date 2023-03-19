# Python 3 code for Pascal's Triangle
# A simple O(n^3)
# program for Pascal's Triangle
def printPascal(n) :
    
	# Iterate through every line
	# and print entries in it
    a = []
    for line in range(0, n) :
		
		# Every line has number of
		# integers equal to line
		# number
        k = []
        for i in range(0, line + 1) :
            k.append(binomialCoeff(line, i))
        a.append(k)
    print(a)
	

# See https://www.geeksforgeeks.org/space-and-time-efficient-binomial-coefficient/
# for details of this function
def binomialCoeff(n, k) :
    # since C(n, k) = C(n, n - k)
    if(k > n - k):
        k = n - k
        
    # initialize result
    res = 1

    # Calculate value of
    # [n * (n-1) *---* (n-k + 1)] / [k * (k-1) *----* 1]
    for i in range(k):
        res = res * (n - i)
        res = res // (i + 1)
    return res

# Driver program
n = 1
printPascal(n)
