# Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.

class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[0] = 1
        
        for i in range(1, n+1):
            for j in range(i):
                dp[i] += dp[j] * dp[i- 1 - j]
        
        print(dp[n])
        return dp[n]

sol = Solution()
sol.numTrees(5)