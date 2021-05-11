# The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value and the median is the mean of the two middle values.

# For example, for arr = [2,3,4], the median is 3.
# For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
# Implement the MedianFinder class:

# MedianFinder() initializes the MedianFinder object.
# void addNum(int num) adds the integer num from the data stream to the data structure.
# double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.

from heapq import heappush, heappop
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.lo = []  
        self.hi = []

    def addNum(self, num: int) -> None:
        heappush(self.lo, -num)             # lo is maxheap, so -1 * num
        heappush(self.hi, -self.lo[0])      # hi is minheap
        heappop(self.lo)
        
        if len(self.lo) < len(self.hi):
            heappush(self.lo, -self.hi[0])
            heappop(self.hi)

    def findMedian(self) -> float:
        if len(self.lo) > len(self.hi):
            return -self.lo[0]                  
        else:
            return (self.hi[0] - self.lo[0]) / 2  # - as low has -ve values


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()