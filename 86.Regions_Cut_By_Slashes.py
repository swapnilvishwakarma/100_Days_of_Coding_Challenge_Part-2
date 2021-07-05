# An n x n grid is composed of 1 x 1 squares where each 1 x 1 square consists of a '/', '\', or blank space ' '. These characters divide the square into contiguous regions.
# Given the grid grid represented as a string array, return the number of regions.
# Note that backslash characters are escaped, so a '\' is represented as '\\'.

class Solution:
    def regionsBySlashes(self, grid: list) -> int:        
        if not grid:
            return 0
        n = len(grid)
        
        granular = [[' ' for _ in range(n*2)] for _ in range(n*2)]        
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == '/':
                    granular[i*2][j*2+1] = '/'
                    granular[i*2+1][j*2] = '/'
                elif grid[i][j] == '\\':
                    granular[i*2][j*2] = '\\'
                    granular[i*2+1][j*2+1] = '\\'
        m = n*2             
        def noOfRegions(i,j):
            if i < 0 or i >= m or j < 0 or j >= m or granular[i][j] != ' ':
                return
            granular[i][j] = "#"
            noOfRegions(i+1,j) 
            noOfRegions(i-1,j)
            noOfRegions(i,j+1)
            noOfRegions(i,j-1)
            # diagonal has conditions
            if i-1 < 0 or j-1 < 0 or (granular[i-1][j] == '/' and granular[i][j -1] == '/'):
                pass
            else:
                noOfRegions(i-1,j-1) 
            if i+1 >= m or j+1 >= m or (granular[i+1][j] == '/' and granular[i][j+1] == '/'):
                pass
            else:
                noOfRegions(i+1,j+1) 
            if i-1 < 0 or j+1 >= m or (granular[i-1][j] == '\\' and granular[i][j+1] == '\\'):
                pass
            else:
                noOfRegions(i-1,j+1) 
            if i+1 >= m or j-1 < 0 or (granular[i+1][j] == '\\' and granular[i][j-1] == '\\'):
                pass
            else:   
                noOfRegions(i+1,j-1) 
            
            
        count = 0
        for i in range(m):
            for j in range(m):
                if granular[i][j] == ' ':
                    noOfRegions(i,j)
                    count+=1
                    
        return count