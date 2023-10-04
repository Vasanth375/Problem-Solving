class MyHashMap:

    def __init__(self):
        self.mydic = []

    def put(self, key: int, value: int):
        for i in self.mydic:
            if key == i[0]:
                i[1] = value
                return
        self.mydic.append([key,value])

    def get(self, key: int):
        for i in self.mydic:
            if key == i[0]:
                return i[1]
        return -1

    def remove(self, key: int):
        for i in range(len(self.mydic)):
            k = self.mydic[i]
            if k[0] == key:
                self.mydic.pop(i)
                return
obj = MyHashMap()
obj.put(1,1)
obj.put(2,2)
obj.put(1,3)
param_2 = obj.get(1)
param_2 = obj.get(3)
print(param_2)
obj.remove(1)