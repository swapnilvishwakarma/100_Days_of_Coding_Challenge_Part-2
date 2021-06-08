# Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order.
# You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.

from collections import Counter
from functools import reduce

class Solution:
    def singleNumber(self, nums: list) -> list:
        # Regular Approach        
        # d = {}
        # o = []
        # count = dict(Counter(nums))
        # for key in count:
        #     if count[key] == 1:
        #         o.append(key)
        # return o

        # Using Bitwise Operator
        xor = lambda x,y : x^y
        xor_result = reduce(xor, nums)
        # mask is the right-most 1 of xor result
        # use mask to separate nums into two groups, one group contains single_num_a, the other contains single_num_b
        mask = xor_result & -xor_result
        single_num_a, single_num_b = 0, 0
        for number in nums:
            # separate and collect these two single numbers by masking
            if mask&number:
                single_num_a ^= number
            else:
                single_num_b ^= number
                
        return [single_num_a, single_num_b]