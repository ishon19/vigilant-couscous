# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return float("-inf")
        
        # bfs solution
        # q = collections.deque()
        # q.append((root))
        # itr = []
        # while q:
        #     level = []
        #     for i in range(len(q)):
        #         node = q.popleft()
        #         level.append(node.val)
        #         if node.left:
        #             q.append((node.left))
        #         if node.right:
        #             q.append((node.right))
        #     itr.append(level)
        # print(itr)
        # return itr[-1][0]

        # dfs approach
        res = (root.val, 0)
        def helper(node, level):
            nonlocal res
            if node: 
                if not node.left and not node.right:
                    if level > res[1]:
                        res = (node.val, level)
                helper(node.left, level + 1)
                helper(node.right, level + 1)
        
        helper(root, 0)
        return res[0]
            
        
        return helper(root)
        
