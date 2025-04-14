# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        if not s:
            return None
        
        cur_idx = [0]

        def dfs():
            if cur_idx[0] >= len(s):
                return None
            
            start = cur_idx[0]
            if s[cur_idx[0]] == "-":
                cur_idx[0] += 1
            while cur_idx[0] < len(s) and s[cur_idx[0]].isdigit():
                cur_idx[0] += 1
            
            node_val = int(s[start:cur_idx[0]])
            node = TreeNode(node_val)

            if cur_idx[0] < len(s) and s[cur_idx[0]] == '(':
                cur_idx[0] += 1
                node.left = dfs()
                cur_idx[0] += 1

            if cur_idx[0] < len(s) and s[cur_idx[0]] == '(':
                cur_idx[0] += 1
                node.right = dfs()
                cur_idx[0] += 1

            return node

        return dfs() 
        