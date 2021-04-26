# Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Implement KthLargest class:
# KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
# int add(int val) Returns the element representing the kth largest element in the stream.

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k
        for i in nums:
            if len(self.heap) < k:
                heapq.heappush(self.heap, i)
            else:
                if i > self.heap[0]:
                    heapq.heappushpop(self.heap, i)
                
    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        else:
            if val > self.heap[0]:
                heapq.heappushpop(self.heap, val)
        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)