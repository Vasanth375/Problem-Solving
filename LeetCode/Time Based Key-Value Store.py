class TimeMap:
    def __init__(self):
        self.data = {}

    def set(self, key: str, value: str, timestamp: int):
        k = self.data.keys()
        if key not in k:
            self.data[key] = []
        self.data[key].append([value, timestamp])

    def get(self, key: str, timestamp: int):
        '''Using Binary Search approach we reduced the number of steps of get function'''
        res, values = "", self.data.get(key, [])
        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return res


obj = TimeMap()
obj.set("foo", "bar", 1)
print(obj.get("foo", 1))
param_2 = obj.get("foo", 3)
print(param_2)
obj.set("foo", "bar2", 4)
print(obj.get("foo", 4))
print(obj.get("foo", 5))
