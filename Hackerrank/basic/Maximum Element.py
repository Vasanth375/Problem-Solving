operations = ["1 23", "1 24", "1 28", "1 10", "2", "3", "2", "2", "3"]
operations = ["1 97", "2", "1 20", "2", "1 26", "1 20", "2", "3", "1 91", "3"]

def getMAx():
    stack = []
    final = [0]
    currMax = 0
    for k in operations:
        kInt = k.split(" ")
        currMax = final[-1]
        if kInt[0] == "1":
            stack.append(int(kInt[1]))

            ## comparing the current max value and currently pointing value
            ## >= means if the stack contains duplicates this is make it as single value
            if int(kInt[1]) >= currMax:
                final.append(int(kInt[1]))
        elif kInt[0] == "2":
            ## popping the stack value and final value if popped value is equal to current max value
            if stack.pop() == currMax:
                final.pop()
        else:
            # yield currMax
            pass
            
    print(final)

getMAx()