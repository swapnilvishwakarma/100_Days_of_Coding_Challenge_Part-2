# There are two types of soup: type A and type B. Initially we have n ml of each type of soup. There are four kinds of operations:

# Serve 100 ml of soup A and 0 ml of soup B
# Serve 75 ml of soup A and 25 ml of soup B
# Serve 50 ml of soup A and 50 ml of soup B
# Serve 25 ml of soup A and 75 ml of soup B
# When we serve some soup, we give it to someone and we no longer have it. Each turn, we will choose from the four operations with equal probability 0.25. If the remaining volume of soup is not enough to complete the operation, we will serve as much as we can. We stop once we no longer have some quantity of both types of soup.

# Note that we do not have the operation where all 100 ml's of soup B are used first.
# Return the probability that soup A will be empty first, plus half the probability that A and B become empty at the same time.

from functools import lru_cache

class Solution:
    def soupServings(self, n: int) -> float:
        if n > 5000: return 1   # shortcut for large N (accurate to 1e-6)
        
        @lru_cache(None)
        def dp(a, b):
            if a <= 0 and b <= 0: return 0.5
            if a <= 0: return 1
            if b <= 0: return 0
            return (dp(a-100, b) + dp(a-75, b-25) + dp(a-50, b-50) + dp(a-25, b-75)) / 4
        
        return dp(n, n)