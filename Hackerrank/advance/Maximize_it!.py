k,m = input().split()
k,m = int(k), int(m)

list = []
mini_lst = []
main_lst = []
sum_lst = []
for i in range(3):
    mini_lst = [int(x) for x in input().split()]
    list.append(mini_lst)

# print(list)

for i in list:
    i.sort(reverse=True)
    main_lst.append(i[0])

for i in main_lst:
    sum_lst.append(i**2)

print(sum(sum_lst)%m)
# a = [1, 2, 9 , 3, 7]
# a.sort(reverse=True)
# print(a)