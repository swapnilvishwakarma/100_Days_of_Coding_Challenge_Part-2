# Implement BFS/Level Order Tree Traversal

class TreeNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

def LevelOrder(root):
    if not root:
        return
    
    queue = []

    queue.append(root)
    while (len(queue) > 0):
        print(queue[0].val)
        node = queue.pop(0)

        if node.left:
            queue.append(node.left)
        
        if node.right:
            queue.append(node.right)


# Driver Code
root = TreeNode(1)
root.left = TreeNode(2)
root.right     = TreeNode(3)
root.left.left  = TreeNode(4)
root.left.right  = TreeNode(5)

print ("Level Order Traversal of binary tree is:")
LevelOrder(root)