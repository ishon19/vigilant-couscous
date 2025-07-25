# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0 
        
        max_width = 0

        q = deque([(root, 0)])

        while q:
            level_size = len(q)
            _, parent_index = q[0]

            for _ in range(level_size):
                node, node_index = q.popleft()

                if node.left:
                    q.append((node.left, 2 * node_index))
                if node.right:
                    q.append((node.right, 2 * node_index + 1))
            
            max_width = max(max_width, node_index - parent_index + 1)

        return max_width 