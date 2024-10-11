# Continue
intervals = [[1,3],[6,9]]
newInterval = [2,5]

# intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
# newInterval = [4,8]


s = newInterval[0]
e = newInterval[1]
newIntervals = []
n = len(intervals)
i = 0
k = intervals[i]
while i < n and k[1] < s:
    if k[1] < s:
        newIntervals.append(k)
    i += 1
    k = intervals[i]

while i < n and k[0] <= e:
    if k[0] <= e:
        newInterval[0] = min(newInterval[0], k[0])
        newInterval[1] = max(newInterval[1], k[1])
    i += 1
    k = intervals[i]
newIntervals.append(newInterval)
newIntervals.extend(intervals[i:])
print(newIntervals)
