# In an infinite binary tree where every node has two children, the nodes are labelled in row order.
# In the odd numbered rows (ie., the first, third, fifth,...), the labelling is left to right, while in the even numbered rows (second, fourth, sixth,...), the labelling is right to left.
# Given the label of a node in this tree, return the labels in the path from the root of the tree to the node with that label.

from math import log
from collections import deque

class Solution:
    def pathInZigZagTree(self, label: int) -> list:
        level = int(log(label, 2))
        solution = deque()
        
        for l in range(level, -1, -1):
            solution.appendleft(label)
            label = (3*(2**l) - 1 - label) // 2
            
        return solution