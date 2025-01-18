# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self._push_left(root)
    
    def  _push_left(self, node):
        if not node:
            return

        while node:
            self.stack.append(node)
            node = node.left
        
    def next(self) -> int:
        top = self.stack.pop()

        if top.right:
            # append the left side of the tree
            self._push_left(top.right)
        
        return top.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()