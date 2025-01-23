#
# @lc app=leetcode id=2471 lang=python3
#
# [2471] Minimum Number of Operations to Sort a Binary Tree by Level
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinSwapsNeeded(self, arr):
        idx_arr = sorted(enumerate(arr), key=lambda x: x[1])
        seen = [False] * len(arr)
        swaps = 0

        for i in range(len(arr)):
            if seen[i] or idx_arr[i][0] == i:
                continue
            
            cycle_len = 0
            j = i
            while not seen[j]:
                seen[j] = True
                j = idx_arr[j][0]
                cycle_len += 1
            
            if cycle_len:
                swaps += (cycle_len - 1)
        
        return swaps
    
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        if not root:
            return root
        
        res = 0
        
        q = deque([root])

        while q:
            level = []

            for _ in range(len(q)):
                node = q.popleft()

                if node:
                    level.append(node.val)
                
                    q.append(node.left)
                    q.append(node.right)
        
            res += self.getMinSwapsNeeded(level)
        
        return res        
        
# @lc code=end

