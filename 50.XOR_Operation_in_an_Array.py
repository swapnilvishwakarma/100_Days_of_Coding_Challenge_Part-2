# Given an integer n and an integer start.
# Define an array nums where nums[i] = start + 2*i (0-indexed) and n == nums.length.
# Return the bitwise XOR of all elements of nums.

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = []
        result = 0
        for i in range(n):
            nums.append(start + 2*i)
            result = result ^ nums[i]
        
        return result