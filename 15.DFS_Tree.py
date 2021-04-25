# Implement DFS Preorder, Inorder and Postorder Tree Traversal

class TreeNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

# Preorder
def pre(root):
    if root:
        print(root.val)

        pre(root.left)
        pre(root.right)

# Inorder
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

# Postorder
def post(root):
    if root:
        post(root.left)
        post(root.right)
        print(root.val)


# Driver Code
root = TreeNode(1)
root.left = TreeNode(2)
root.right     = TreeNode(3)
root.left.left  = TreeNode(4)
root.left.right  = TreeNode(5)

print("Preorder traversal of binary tree is")
pre(root)
  
print("\nInorder traversal of binary tree is")
inorder(root)
  
print("\nPostorder traversal of binary tree is")
post(root)