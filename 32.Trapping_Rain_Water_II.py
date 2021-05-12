# Given an m x n integer matrix heightMap representing the height of each unit cell in a 2D elevation map, return the volume of water it can trap after raining.

import heapq
class Solution:
    def trapRainWater(self, heightMap: list) -> int:
        n, m = len(heightMap), len(heightMap[0])
        h = []
        queued = [[0 for c in range(m)] for r in range(n)]
        seen = [[0 for c in range(m)] for r in range(n)]
        mx = 0
        total = 0
        
        def enqueue(i, j):
            if not queued[i][j] and not seen[i][j]:
                heapq.heappush(h, [heightMap[i][j], i, j])
                queued[i][j] = 1
                
        def enqueue_neighbors(i, j):
            if i >= n or j >= m:
                return []
            if i != 0:
                enqueue(i-1, j)
            if i != n-1:
                enqueue(i+1, j)
            if j != 0:
                enqueue(i, j-1)
            if j != m-1:
                enqueue(i, j+1)

        for j in range(m):
            enqueue(0, j)
            enqueue(n-1, j)
        for i in range(n):
            enqueue(i, 0)
            enqueue(i, m-1)
        
        while h:
            val, i, j = heapq.heappop(h)
            if val < mx:
                total += mx - val
            mx = max(mx, val)
            seen[i][j] = 1
            enqueue_neighbors(i, j)
        
        return total