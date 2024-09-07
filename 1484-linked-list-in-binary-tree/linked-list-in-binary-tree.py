# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        paths = []

        def traverse(node, path):
            if node: 
                if not node.left and not node.right:
                    paths.append("".join(path + [str(node.val)]))
                    return
                traverse(node.left, path + [str(node.val)])
                traverse(node.right, path + [str(node.val)])
        
        traverse(root, [])
        
        ll = ''
        ptr = head
        while ptr:
            ll += str(ptr.val)
            ptr = ptr.next

        for path in paths:
            if ll in path:
                return True
        return False