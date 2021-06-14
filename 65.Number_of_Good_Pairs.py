# Given an array of integers nums.
# A pair (i,j) is called good if nums[i] == nums[j] and i < j.
# Return the number of good pairs.

class Solution:
    def numIdenticalPairs(self, nums: list) -> int:
        # Method 1
        # count = 0
        # for i, val1 in enumerate(nums):
        #     for j, val2 in enumerate(nums):
        #         if i < j and val1 == val2:
        #             count += 1
        # return count
    
        # Method 2
        hashMap = {}
        res = 0
        for number in nums:            
            if number in hashMap:
                res += hashMap[number]
                hashMap[number] += 1
            else:
                hashMap[number] = 1
        return res