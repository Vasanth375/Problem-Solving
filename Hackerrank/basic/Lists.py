if __name__ == '__main__':
    # given a N number of inputs called commands like append, insert, print, etc.
    N = int(input())
    Lists = []  # list to do operations
    for i in range(N):
        # inputing the command and its associated values
        command = list(map(str, input().split()))

        # checking the condition and performing the operation
        if command[0] == "append":
            Lists.append(int(command[1]))
        elif (command[0] == "insert"):
            Lists.insert(int(command[1]), int(command[2]))
        elif command[0] == "print":
            print(Lists)
        elif command[0] == "remove":
            Lists.remove(int(command[1]))
        elif command[0] == "sort":
            Lists.sort()
        elif command[0] == "pop":
            Lists.pop()
        elif command[0] == "reverse":
            Lists.reverse()