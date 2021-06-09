# Given 3 positives numbers a, b and c. Return the minimum flips required in some bits of a and b to make ( a OR b == c ). (bitwise OR operation).
# Flip operation consists of change any single bit 1 to 0 or change the bit 0 to 1 in their binary representation.

class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        count = 0
        while a or b or c:
            if (a & 1) | (b & 1) != (c & 1):
                if (c & 1): count += 1
                else: count += (a & 1) + (b & 1)
            a, b, c = a >> 1, b >> 1, c >> 1
            
        return count