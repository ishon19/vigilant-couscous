# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        q = deque([root])
        flip = False

        while q:
            level = [] 

            for _ in range(len(q)):
                node = q.popleft()
                if not node:
                    continue

                if flip:
                    level.append(node)
                q.append(node.left)
                q.append(node.right)
            
            if level: 
                l, r = 0, len(level)-1
                while l <= r:
                    level[l].val, level[r].val = level[r].val, level[l].val
                    l += 1
                    r -= 1

            flip = not flip

        return root
            
                
