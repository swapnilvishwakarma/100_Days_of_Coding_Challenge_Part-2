# Given the root of a binary tree, return the bottom-up level order traversal of its nodes' values. (i.e., from left to right, level by level from leaf to root).

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        queue = [root]
        result = []
        
        while len(queue) != 0:
            layer = []
            for i in range(len(queue)):
                temp = queue.pop(0)
                layer.append(temp.val)
                if temp.left != None:
                    queue.append(temp.left)
                if temp.right != None:
                    queue.append(temp.right)
            result.insert(0, layer)
            
        return result