# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: list, k: int) -> list:
        # O(1) time 
        if k == len(nums):
            return nums
        
        # 1. build hash map : character and how often it appears
        # O(N) time
        count = Counter(nums)
        
        # 2-3. build heap of top k frequent elements and
        # convert it into an output array
        # O(N log k) time
        ans = heapq.nlargest(k, count.keys(), key=count.get)
        print(ans)
        return ans

sol = Solution()
sol.topKFrequent([1,1,1,2,2,3], k = 2)