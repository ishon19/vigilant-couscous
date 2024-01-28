# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        traversal = collections.defaultdict(list)
        queue = collections.deque()
        queue.append([root, 0])

        while queue:
            node, offset = queue.popleft()
            if node:
                queue.append([node.left, offset - 1])
                queue.append([node.right, offset + 1])
                traversal[offset].append(node.val)
        
        # print('traversed', traversal)

        return [traversal[k] for k in sorted(traversal.keys())]