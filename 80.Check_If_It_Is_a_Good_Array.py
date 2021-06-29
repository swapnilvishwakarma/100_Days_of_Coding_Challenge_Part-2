# Given an array nums of positive integers. Your task is to select some subset of nums, multiply each element by an integer and add all these numbers. The array is said to be good if you can obtain a sum of 1 from the array by any possible subset and multiplicand.
# Return True if the array is good otherwise return False.

from math import gcd

class Solution:
    def isGoodArray(self, nums: list) -> bool:
        g = nums[0]
        
        for i in nums[1:]:
            g = gcd(g, i)
        
        return g == 1