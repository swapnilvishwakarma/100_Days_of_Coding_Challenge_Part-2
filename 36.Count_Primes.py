# Count the number of prime numbers less than a non-negative number, n.
import math

class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        
        numbers = {}
        for p in range(2, int(math.sqrt(n)) + 1):
            if p not in numbers:
                for multiple in range(p*p, n, p):
                    numbers[multiple] = 1
        
        # Exclude "1" and the number "n" itself.
        return n - len(numbers) - 2