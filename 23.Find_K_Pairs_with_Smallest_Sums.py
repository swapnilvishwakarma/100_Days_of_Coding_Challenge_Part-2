# You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.
# Define a pair (u, v) which consists of one element from the first array and one element from the second array.
# Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.

import heapq

class Solution:
    def kSmallestPairs(self, nums1: list, nums2: list, k: int):
        if not nums1 or not nums2 or not k: return []
        i = j = 0
        minHeap = []
        
        for _ in range(k):
            if i < len(nums1) and j < len(nums2):
                if nums1[i] <= nums2[j]:
                    for x in nums2[j:]: heapq.heappush(minHeap, (nums1[i], x))
                    i += 1
                else:
                    for x in nums1[i:]: heapq.heappush(minHeap, (x, nums2[j]))
                    j += 1

        print(heapq.nsmallest(k, minHeap, key = sum))            
        return heapq.nsmallest(k, minHeap, key = sum)

sol = Solution()
sol.kSmallestPairs(nums1 = [1,1,2], nums2 = [1,2,3], k = 2)