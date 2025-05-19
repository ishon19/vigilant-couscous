# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        offset_map = defaultdict(list)

        q = deque([(root, 0)])
        min_offset = 0
        max_offset = 0

        while q:
            node, offset = q.popleft()

            offset_map[offset].append(node.val)
            min_offset = min(min_offset, offset)
            max_offset = max(max_offset, offset)

            if node.left:
                q.append((node.left, offset-1))
            
            if node.right:
                q.append((node.right, offset+1))

        res = []
        for offset in range (min_offset, max_offset+1):
            res.append(offset_map[offset])
        
        return res

            
