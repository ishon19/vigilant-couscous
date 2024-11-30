# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        def dfs(node):
            if not node:
                res.append('x')
                return res
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return " ".join(res)
            
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def dfs(node):
            s = next(node)
            if s == 'x':
                return None
            cur = TreeNode(s)
            cur.left = dfs(node)
            cur.right = dfs(node)
            return cur
        return dfs(iter(data.split()))
            
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))