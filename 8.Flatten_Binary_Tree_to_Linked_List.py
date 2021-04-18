# Given the root of a binary tree, flatten the tree into a "linked list":

# The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
# The "linked list" should be in the same order as a pre-order traversal of the binary tree.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: TreeNode):
        """
        Do not return anything, modify root in-place instead.
        """
        if root is not None:
            self.flatten(root.left)
            self.flatten(root.right)
            
            if root.left is not None:
                current = root.left
                while current.right is not None:
                    current = current.right
                current.right = root.right
                root.right = root.left
                root.left = None
                
        return root

def printPreorder(root):
    if root is None:
        return
    print(root.val)
    printPreorder(root.left)
    printPreorder(root.right)

# [1,2,5,3,4,null,6]
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(None)
root.right.right = TreeNode(6)
sol = Solution()
sol.flatten(root)
print(printPreorder(root))