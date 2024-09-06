# n = 6
# start= [1, 3,9, 0, 5, 8, 5]
# end=  [2, 4,10,  6, 7, 9, 9]

# # n = 3
# # start= [10, 12, 20]
# # end= [20, 25, 30]

# class meeting:
#     def __init__(self, start, end, pos):
#         self.start = start
#         self.end = end
#         self.pos = pos


# for i in range(len(end)):
#     for j in range(i+1, len(end)):
#         if end[i] > end[j]:
#             end[i], end[j] = end[j], end[i]
#             start[i], start[j] = start[j], start[i]

# count = 1
# lasttime = end[0]
# res = [0]

# for i in range(1, len(end)):
#     if start[i] > lasttime:
#         count += 1
#         res.append(i)
#         lasttime = end[i]
# print(res, count)


def maxMeetings(s, e, n: int) -> None:
    lis = []
    for i in range(0, n):
        lis.append((start[i], end[i]))
    lis.sort(key = lambda x : x[1])
    # print(lis)
    ans = 0
    count = 0
    for st, en in lis:
        if st > ans:
            ans = en
            count += 1
    return count


n = 6
start = [1, 3, 0, 5, 8, 5]
end = [2, 4, 5, 7, 9, 9]
start = [75250 ,50074 ,43659 ,8931 ,11273 ,27545, 50879, 77924]
end = [112960 ,114515 ,81825 ,93424 ,54316 ,35533 ,73383 ,160252]
print(maxMeetings(start, end, n))
