# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.

class Solution:
    def singleNumber(self, nums: list) -> int:
        
#         hashtable = {}
#         for num in nums:
#             if num in hashtable:
#                 hashtable[num] += 1
#             else:
#                 hashtable[num] = 1
        
#         def get_key(val):
#             for key, value in hashtable.items():
#                 if val == value:
#                     return key
                
#         return get_key(1)
    
    # Using Bit Manipulation
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        for i in nums:
            a ^= i
        return a