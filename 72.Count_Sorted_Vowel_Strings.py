# Given an integer n, return the number of strings of length n that consist only of vowels (a, e, i, o, u) and are lexicographically sorted.
# A string s is lexicographically sorted if for all valid i, s[i] is the same as or comes before s[i+1] in the alphabet.

class Solution:
    def countVowelStrings(self, n: int) -> int:
        # Pattern Approach
        # def helper(n, vowel):
        #     if n == 0:
        #         return 1
            
        #     res = 0
        #     for i in range(vowel, 5):
        #         res += helper(n-1, i)
        #     return res
        
        # return helper(n, 0)
    
        # DP Approach
        dp = [[i for i in range(5,0,-1)] for _ in range(n)]   # intialize dp matrix
        for i in range(1,n):
            for j in range(3,-1,-1):
                dp[i][j] = dp[i - 1][j] + dp[i][j + 1]   # dp expression
                
        return dp[n-1][0]