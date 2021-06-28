# Alice and Bob take turns playing a game, with Alice starting first.
# Initially, there are n stones in a pile.  On each player's turn, that player makes a move consisting of removing any non-zero square number of stones in the pile.
# Also, if a player cannot make a move, he/she loses the game.
# Given a positive integer n. Return True if and only if Alice wins the game otherwise return False, assuming both players play optimally.

import math

class Solution:
    # @lru_cache(None)
    def winnerSquareGame(self, n: int) -> bool:
        # if n == 0:
        #     return False
        
        # for x in range(1, math.floor(math.sqrt(n)) + 1):
        #     if not self.winnerSquareGame(n - (n * n)):
        #         return True
        # return False
    
        dp = [False] * (n + 1)
        
        for i in range(1, n + 1):
            for k in range(1, int(i ** 0.5) + 1):
                if dp[i - k * k] == False:
                    dp[i] = True
                    break
        return dp[n]