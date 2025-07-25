# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class BSTIterator:
    def __init__(self, root):
        self.root = root
        self.stack = []
        self._push_left_node(root)

    def _push_left_node(self, node):
        ptr = node
        while ptr:
            self.stack.append(ptr)
            ptr = ptr.left

    def next(self):
        node = self.stack.pop()
        val = node.val
        if node.right:
            self._push_left_node(node.right)
        return val
    
    def hasNext(self):
        return len(self.stack) != 0
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()