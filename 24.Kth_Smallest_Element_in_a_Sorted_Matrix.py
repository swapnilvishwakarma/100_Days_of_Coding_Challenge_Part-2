# Given an n x n matrix where each of the rows and columns are sorted in ascending order, return the kth smallest element in the matrix.
# Note that it is the kth smallest element in the sorted order, not the kth distinct element.

import heapq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        if not matrix or not matrix[0]:
            return -1
        
        heap = []
        
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                nextVal = -matrix[row][col]
                if len(heap) < k:
                    heapq.heappush(heap, nextVal)
                elif nextVal > heap[0]:
                    heapq.heappushpop(heap, nextVal)
                    
        return -heap[0]