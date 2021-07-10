# On a 2D plane, we place n stones at some integer coordinate points. Each coordinate point may have at most one stone.
# A stone can be removed if it shares either the same row or the same column as another stone that has not been removed.
# Given an array stones of length n where stones[i] = [xi, yi] represents the location of the ith stone, return the largest possible number of stones that can be removed.

from collections import defaultdict

class Solution:
    def removeStones(self, stones: list) -> int:
        n = len(stones)
        groupByX = defaultdict(list)
        groupByY = defaultdict(list)
        
        for i in range(len(stones)):
            x, y = stones[i]
            groupByX[x].append(i)
            groupByY[y].append(i)
            
        
        disjointSet = 0
        visited = set()
        
        for i in range(len(stones)):
            if i in visited: continue
            stack = [i]
            disjointSet += 1
            
            while stack:
                current = stack.pop()
                visited.add(current)
                x, y = stones[current]
                
                for next_i in groupByX[x]:
                    if next_i in visited: continue
                    stack.append(next_i)
                    
                for next_i in groupByY[y]:
                    if next_i in visited: continue
                    stack.append(next_i)
                
        return n - disjointSet