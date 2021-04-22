# You are given the root of a binary search tree (BST), where exactly two nodes of the tree were swapped by mistake. Recover the tree without changing its structure.
# Follow up: A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        curr = root
        prev = TreeNode(float('-inf'))
        replace = []
        stack = []
        
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            
            temp = stack.pop()
            
            if temp.val < prev.val:
                replace.append((prev, temp))
            
            prev = temp
            curr = temp.right
        
        replace[0][0].val, replace[-1][1].val = replace[-1][1].val, replace[0][0].val