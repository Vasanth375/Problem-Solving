s = "is2 sentence4 This1 a3"

m = s.split(" ")

k = [""] * len(m)

for j in range(1, len(m) + 1):
    for i in m:
        if int(i[-1]) == j:
            k.append(i[: len(i) - 1])
print(" ".join(k))

# ## Optimised version of the problem
# for i in m:
#     k[int(i[-1]) - 1] = i[:-1]
# print(k)
