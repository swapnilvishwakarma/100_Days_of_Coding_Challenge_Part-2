# On a 2 dimensional grid with rows rows and cols columns, we start at (rStart, cStart) facing east.
# Here, the north-west corner of the grid is at the first row and column, and the south-east corner of the grid is at the last row and column.
# Now, we walk in a clockwise spiral shape to visit every position in this grid. 
# Whenever we would move outside the boundary of the grid, we continue our walk outside the grid (but may return to the grid boundary later.) 
# Eventually, we reach all rows * cols spaces of the grid.
# Return a list of coordinates representing the positions of the grid in the order they were visited.

class Solution(object):
    def spiralMatrixIII(self, R, C, r0, c0):
        ans = [(r0, c0)]
        if R * C == 1: return ans

        # For walk length k = 1, 3, 5 ...
        for k in range(1, 2*(R+C), 2):

            # For direction (dr, dc) = east, south, west, north;
            # and walk length dk...
            for dr, dc, dk in ((0, 1, k), (1, 0, k), (0, -1, k+1), (-1, 0, k+1)):

                # For each of dk units in the current direction ...
                for _ in range(dk):

                    # Step in that direction
                    r0 += dr
                    c0 += dc

                    # If on the grid ...
                    if 0 <= r0 < R and 0 <= c0 < C:
                        ans.append((r0, c0))
                        if len(ans) == R * C:
                            return ans


# class Solution:
#     def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        
#         dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
#         dir_idx = 0
#         total = rows * cols
#         steps = 1
#         inc = 1
#         result = [(rStart, cStart)]
        
#         while len(result) < total:
#             for i in range(inc):
#                 rStart, cStart = rStart + dirs[dir_idx[0], cStart + dirs[dir_idx[1]]
#                 if rStart >= 0 and rStart < rows and cStart >= 0 and cStart < cols:
#                     result.append([rStart, cStart])
            
#             dir_idx = (dir_idx + 1) % 4
#             if steps % 2 == 0:
#                 inc += 1
#             steps += 1
        
#         return result