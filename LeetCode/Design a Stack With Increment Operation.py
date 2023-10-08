class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.size = maxSize

    def push(self, x: int) -> None:
        if len(self.stack) < self.size:
            self.stack.append(x)

    def pop(self) -> int:
        if len(self.stack) == 0:
            return -1
        return self.stack.pop()

    def increment(self, k: int, val: int) -> None:
        if self.size < k:
            for i in range(len(self.stack)):
                self.stack[i] += val
        elif self.size >= k:
            i = 0
            while i < k and i < len(self.stack):
                self.stack[i] += val
                i += 1

    def display(self):
        print(self.stack)


cus = CustomStack(12)
cus.push(83)
cus.increment(2,60)
cus.increment(9,61)
cus.increment(1,60)
cus.push(82)
cus.push(21)
cus.push(58)
cus.increment(8,8)
cus.push(22)
cus.push(80)
cus.increment(1, 64)
print(cus.pop())
print(cus.pop())
cus.push(24)


# cus.push(2)
# cus.push(3)
# cus.push(4)
# cus.display()
# cus.increment(5,100)
# cus.increment(2,100)
# print(cus.pop())
# print(cus.pop())
# print(cus.pop())
# print(cus.pop())