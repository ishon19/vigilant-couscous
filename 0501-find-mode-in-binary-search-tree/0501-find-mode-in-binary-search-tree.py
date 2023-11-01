# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
         q = collections.deque([root])
         res = []

         while q:
             node = q.popleft()
             if node:
                 res.append(node.val)
             if node.left:
                 q.append(node.left)
             if node.right:
                 q.append(node.right)
         counts = collections.Counter(res)
         temp = sorted([[k,v] for k,v in counts.items()], key=lambda e: e[1], reverse=True)
         ans = [temp[0][0]]
         # print(temp)
         for i, [k,v] in enumerate(temp):
             if i == 0:
                 continue
             else:
                 if v == temp[0][1]:
                     ans.append(k)
         return ans