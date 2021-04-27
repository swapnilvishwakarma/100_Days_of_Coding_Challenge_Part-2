# We have a collection of stones, each stone has a positive integer weight.

# Each turn, we choose the two heaviest stones and smash them together.  Suppose the stones have weights x and y with x <= y.  The result of this smash is:

# If x == y, both stones are totally destroyed
# If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
# At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)

import heapq

class Solution:
    def lastStoneWeight(self, stones: list) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            stone1 = -(heapq.heappop(stones))
            stone2 = -(heapq.heappop(stones))
            
            if stone1 == stone2:
                continue
            heapq.heappush(stones, -(abs(stone1 - stone2)))
        
        if len(stones) == 0:
            return 0
        
        # print(-(heapq.heappop(stones)))
        return -(heapq.heappop(stones))

sol = Solution()
sol.lastStoneWeight([8,1,2,3,4,6])