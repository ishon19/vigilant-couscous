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
        
        offsetMap = defaultdict(list)
        q = deque([(root, 0)])
        minOffset, maxOffset = 0, 0 

        while q:
            node, offset = q.popleft()
            offsetMap[offset].append(node.val)
            minOffset = min(minOffset, offset)
            maxOffset = max(maxOffset, offset)

            if node.left:
                q.append((node.left, offset - 1))            
            if node.right:
                q.append((node.right, offset + 1))

        res = []
        for offset in range(minOffset, maxOffset + 1):
            res.append(offsetMap[offset])
        return res