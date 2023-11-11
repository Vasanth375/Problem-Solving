from collections import defaultdict
adjacentPairs = [[2, 1], [3, 4], [3, 2]]
# adjacentPairs = [[4, -2], [1, 4], [-3, 1]]
# adjacentPairs = [[4, -10], [-1, 3], [4, -3], [-3, 3]]
adjacentPairs = [[-3, -9], [-5, 3], [2, -9],
                 [6, -3], [6, 1], [5, 3], [8, 5], [-5, 1], [7, 2]]
graph = defaultdict(list)

# creating a adjacency list for all the values in the adjacent pairs
for x, y in adjacentPairs:
    graph[x].append(y)
    graph[y].append(x)

root = None
# finding the root value where the length of the value is 1
for num in graph:
    if len(graph[num]) == 1:
        root = num
        break

# using Depth first search we are searching the node where prev and current node shouldn't be the same


def dfs(node, prev, ans):
    ans.append(node)
    for neighbor in graph[node]:
        if neighbor != prev:
            dfs(neighbor, node, ans)
            # Recursively using the node value we can just traverse through and adding to the answer list


ans = []
dfs(root, None, ans)
print(ans)
