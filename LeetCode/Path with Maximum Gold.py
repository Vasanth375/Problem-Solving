'''
In a gold mine grid of size m x n, each cell in this mine has an integer representing the amount of gold in that cell, 0 if it is empty.

Return the maximum amount of gold you can collect under the conditions:

Every time you are located in a cell you will collect all the gold in that cell.
From your position, you can walk one step to the left, right, up, or down.
You can't visit the same cell more than once.
Never visit a cell with 0 gold.
You can start and stop collecting gold from any position in the grid that has some gold.
'''
# using two approaches we can solve this #DFS using backtrack #BFS using backtrack

# DFS
def getMaximumGold(grid) -> int:
    direct = [0,1,0,-1, 0]
    rows = len(grid)
    cols = len(grid[0])
    maxGold = 0
    def dfsback(grid, rows, cols, row, col):
        # base-case: checking whether we meet any boundary of matrix and if gold is 0 return 0
        if row < 0 or col < 0 or row == rows or col == cols or grid[row][col] == 0:
            return 0
            
        maxGold = 0

        # marking as 0 when visited
        originV = grid[row][col]
        grid[row][col] = 0

        # visiting all adjacent directions 
        for dir in range(4):
            maxGold = max(maxGold, dfsback(grid, rows, cols, direct[dir]+row, direct[dir+1]+col))

        # set values back to original value
        grid[row][col] = originV
        return maxGold + originV
    
    # search for the path with maximum gold starting from each cell
    for row in range(rows):
        for col in range(cols):
            maxGold = max(maxGold, dfsback(grid, rows, cols, row, col))
    return maxGold

from collections import deque

def getMaxGoldBFS(grid) -> int:
    direct = [0,1,0,-1, 0]
    rows = len(grid)
    cols = len(grid[0])
    totalGold = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] != 0:
                totalGold += grid[row][col]
    maxGold = 0
    def bfsQueue(row, col):
        queue = deque()
        visited = set()
        visited.add((row, col))
        queue.append((row,col, grid[row][col], visited))
        maxGold = 0
        while queue:
            currRow, currCol, currGold, currVis = queue.popleft()
            maxGold = max(maxGold, currGold)            
            for dir in range(4):
                nextRow = currRow + direct[dir]
                nextCol = currCol + direct[dir+1]

                if 0 <= nextRow < rows and 0<= nextCol <cols and grid[nextRow][nextCol] != 0 and (nextRow, nextCol) not in currVis:
                    currVis.add((nextRow, nextCol))
                    queue.append((nextRow, nextCol, currGold+grid[nextRow][nextCol], currVis.copy()))
                    currVis.remove((nextRow, nextCol))
        return maxGold
    
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] != 0:
                maxGold = max(maxGold, bfsQueue(row, col))
                if maxGold == totalGold:
                    return totalGold
    return maxGold