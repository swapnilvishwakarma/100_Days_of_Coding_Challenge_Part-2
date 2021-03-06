# Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where each path's sum equals targetSum.

# A leaf is a node with no children.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        result = []
        path = []
        pathofsum = 0
        self.dfs(root, pathofsum, targetSum, path, result)
        return result
        
    def dfs(self, root, pathofsum, targetSum, path, result):
        if not root:
            return None
        
        pathofsum += root.val
        if root.left is None and root.right is None and pathofsum == targetSum:
            result.append([*path, root.val])
            return None
        
        path.append(root.val)
        self.dfs(root.left, pathofsum, targetSum, path, result)
        self.dfs(root.right, pathofsum, targetSum, path, result)
        pathofsum -= root.val
        path.pop()