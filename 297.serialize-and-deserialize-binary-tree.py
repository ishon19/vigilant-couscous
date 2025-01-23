#
# @lc app=leetcode id=297 lang=python3
#
# [297] Serialize and Deserialize Binary Tree
#

# @lc code=start
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
        def dfs(node):
            if not node:
                pattern.append('x')
                return
            pattern.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        
        pattern = []
        dfs(root)
        return ' '.join(pattern)        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def dfs(node):
            val = next(node)
            if val == 'x':
                return None
            newNode = TreeNode(int(val))
            newNode.left = dfs(node)
            newNode.right = dfs(node)
            return newNode
        
        vals = iter(data.split())
        return dfs(vals)
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# @lc code=end

