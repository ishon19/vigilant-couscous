# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        q = collections.deque([root])
        traversed = []
        while q:
            lvl = []
            for i in range(len(q)):
                node = q.popleft()
                if node: lvl.append(node.val)

                if node and node.left:
                    q.append(node.left)
                if node and node.right:
                    q.append(node.right)
            traversed.append(lvl)
        res = []

        for lvl in traversed:
            if len(lvl): res.append(max(lvl))

        return res
