# You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.
# Return the max sliding window.

import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        
        deque = collections.deque()
        res = []
        
        for i, num in enumerate(nums):
            while(deque and nums[deque[-1]] < num):
                deque.pop()
            if(deque and i - deque[0] >= k):
                deque.popleft()
            deque.append(i)
            res.append(nums[deque[0]])

        return res[k-1:]