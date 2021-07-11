# Given a m x n grid. Each cell of the grid has a sign pointing to the next cell you should visit if you are currently in this cell. The sign of grid[i][j] can be:
# 1 which means go to the cell to the right. (i.e go from grid[i][j] to grid[i][j + 1])
# 2 which means go to the cell to the left. (i.e go from grid[i][j] to grid[i][j - 1])
# 3 which means go to the lower cell. (i.e go from grid[i][j] to grid[i + 1][j])
# 4 which means go to the upper cell. (i.e go from grid[i][j] to grid[i - 1][j])
# Notice that there could be some invalid signs on the cells of the grid which points outside the grid.

# You will initially start at the upper left cell (0,0). A valid path in the grid is a path which starts from the upper left cell (0,0) and ends at the bottom-right cell (m - 1, n - 1) following the signs on the grid. The valid path doesn't have to be the shortest.
# You can modify the sign on a cell with cost = 1. You can modify the sign on a cell one time only.
# Return the minimum cost to make the grid have at least one valid path.


class Solution:
    def minCost(self, grid: list) -> int:
        m, n = len(grid), len(grid[0])
        direct = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        seen = set()
        queue = [(0, 0)]
        cost = 0
        
        while queue: #breadth-first search
            temp = set()
            for i, j in queue: 
                if i == m-1 and j == n-1: return cost
                if 0 <= i < m and 0 <= j < n and (i, j) not in seen: #skip invalid point
                    seen.add((i, j))
                    di, dj = direct[grid[i][j]-1]
                    queue.append((i+di, j+dj))
                    temp |= {(i+di, j+dj) for di, dj in direct}
            queue = list(temp - seen)
            cost += 1