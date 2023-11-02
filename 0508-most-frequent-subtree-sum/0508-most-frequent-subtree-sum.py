# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        hm = collections.defaultdict(int)

        def helper(node):
            if not node: return 0
            l = helper(node.left)
            r = helper(node.right)
            nodesum = l + r + node.val
            hm[nodesum] += 1
            return nodesum
        
        helper(root)

        res = sorted([[k,v] for k,v in hm.items()], key=lambda x: x[1], reverse=True)
        temp = res[0][1]
        ans = [res[0][0]]
        for i, [k,v] in enumerate(res):
            if i == 0:
                continue
            else:
                if v == temp:
                    ans.append(k)
        return ans
