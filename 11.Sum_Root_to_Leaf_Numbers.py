# You are given the root of a binary tree containing digits from 0 to 9 only.
# Each root-to-leaf path in the tree represents a number.
# For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
# Return the total sum of all root-to-leaf numbers.
# A leaf node is a node with no children.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        
        def dfs(root, Sum=0):
            if not root:
                return 0
            if not root.left and not root.right:
                return Sum + root.val
            
            return dfs(root.left, (Sum+root.val)*10) + dfs(root.right, (Sum+root.val)*10)
        
        return dfs(root, 0)