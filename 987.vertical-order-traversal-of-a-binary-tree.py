#
# @lc app=leetcode id=987 lang=python3
#
# [987] Vertical Order Traversal of a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        nodes = defaultdict(list)

        q = deque([(root, 0, 0)])

        while q:
            node, x, y = q.popleft()
            if node:
                heappush(nodes[x], (y, node.val))
                q.append((node.left, x - 1, y + 1))
                q.append((node.right, x + 1, y + 1))
        
        res = []
        for x in sorted(nodes.keys()):
            col = [val for _, val in sorted(nodes[x])]
            res.append(col)
        
        return res

# @lc code=end

