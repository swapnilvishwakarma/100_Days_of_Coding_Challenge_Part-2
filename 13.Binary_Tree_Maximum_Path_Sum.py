# A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.
# The path sum of a path is the sum of the node's values in the path.
# Given the root of a binary tree, return the maximum path sum of any path.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.maximum = float('-inf')
        
        def dfs(root):
            if not root:
                return 0
            
            left_max = max(0, dfs(root.left))
            right_max = max(0, dfs(root.right))
            self.maximum = max(self.maximum, left_max + right_max + root.val)
            
            return max(left_max, right_max) + root.val
        
        dfs(root)
        return self.maximum