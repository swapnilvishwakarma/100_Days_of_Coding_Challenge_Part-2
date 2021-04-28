# Given an integer array nums and an integer k, return the kth largest element in the array.
# Note that it is the kth largest element in the sorted order, not the kth distinct element.

import heapq

class Solution:
    def findKthLargest(self, nums: list, k: int) -> int:
        if not nums or not k or k < 0:
            return None
        
        maxheap, res = [], None
        
        for num in nums:
            heapq.heappush(maxheap, -num)

        for _ in range(k):
            res = -heapq.heappop(maxheap)
        print(res)
        return res

sol = Solution()
sol.findKthLargest([3,2,3,1,2,4,5,5,6], k = 4)