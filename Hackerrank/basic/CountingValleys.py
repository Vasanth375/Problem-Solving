# try again later

steps = 8
path = "UDDDUDUU"
path = "DDUUUUDD"

# Sum 0 means he has crossed a valley or a mountain
# But, whenever he crosses a valley (means when the sum is 0), the previous step is always "U"
# So, for each step , manipulate Sum variable, and whenever the sum is 0 check for the current step("U" or "D").
# If it is "U" a valley has beem crossed and increment valley variable.

def countingValleys(steps, path):
    U=1
    D=-1
    sum=valley =0
    l=m=[]
    for ch in path:
        if(ch == "U"):
            sum+=U
        else:
            sum+=D
        if(sum == 0 and ch == "U"):
            valley+=1
    return valley
print(countingValleys(steps, path))
