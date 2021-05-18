# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

# Note:
# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.

class Solution:
    def isValidSudoku(self, board: list) -> bool:
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        mMat = [set() for i in range(9)]
        
        for i in range(9):
            for j in range(9):
                cur = board[i][j]
                if cur != '.':
                    
                    k = (i // 3 ) * 3 + j // 3
                
                    if cur not in rows[i]:
                        rows[i].add(cur)
                    else:
                        return False
                    
                    if cur not in cols[j]:
                        cols[j].add(cur)
                    else:
                        return False
                
                    if cur not in mMat[k]:
                        mMat[k].add(cur)
                    else:
                        return False
                    
        return True