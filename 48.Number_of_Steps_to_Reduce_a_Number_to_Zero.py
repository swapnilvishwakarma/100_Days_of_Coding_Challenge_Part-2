# Given a non-negative integer num, return the number of steps to reduce it to zero. If the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.

class Solution:
    def numberOfSteps(self, num: int) -> int:
        count = 0
        while num != 0:
            count += 1
            
            if num & 1 == 1:
                # odd number, subtract by 1
                num -= 1

            else:
                # even number, divide by 2 <=> right shift one bit
                num >>= 1
                
        return count