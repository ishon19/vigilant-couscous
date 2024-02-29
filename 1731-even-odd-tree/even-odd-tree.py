# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        q = collections.deque([root])
        levels = []
        itr = 0

        while q:
            level = []
            for i in range(len(q)):
                node = q.popleft()

                if itr % 2 == 0:
                    if node.val % 2 == 0:
                        # print('case 1')
                        return False
                    else:
                        # print('check 2', level and level[-1], node.val)
                        if level and level[-1] >= node.val:
                            print('case 2')
                            return False
                else:
                    if node.val % 2 != 0:
                        # print('case 3')
                        return False
                    else:
                        if level and level[-1] <= node.val:
                            # print('case 4')
                            return False
                
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            levels.append(level)
            itr += 1
        
        # print(levels)
        return True