# Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.
# Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.
# Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        # use level order traversal to match LeetCode's serialization format
        flat_bt = []
        queue = collections.deque([root])
        while queue:
            node = queue.pop()
            if node:
                flat_bt.append(str(node.val))
                queue.appendleft(node.left)
                queue.appendleft(node.right)
            else:
                # you can use any char to represent null
                # empty string means test for a non-null node is simply: flat_bt[i]
                flat_bt.append('')
        return ','.join(flat_bt)


    def deserialize(self, data):
        if not data:
            return
        flat_bt = data.split(',')
        ans = TreeNode(flat_bt[0])
        queue = collections.deque([ans])
        i = 1
        # when you pop a node, its children will be at i and i+1
        while queue:
            node = queue.pop()
            if i < len(flat_bt) and flat_bt[i]:
                node.left = TreeNode(int(flat_bt[i]))
                queue.appendleft(node.left)
            i += 1
            if i < len(flat_bt) and flat_bt[i]:
                node.right = TreeNode(int(flat_bt[i]))
                queue.appendleft(node.right)
            i += 1
        return ans

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))