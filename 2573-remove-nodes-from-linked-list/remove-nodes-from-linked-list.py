# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = []

        ptr = head
        while ptr:
            nodes.append(ptr)
            ptr = ptr.next
        
        final = []
        for node in nodes:
            while final and node.val > final[-1].val:
                final.pop()
            final.append(node)
        
        if not final:
            return None
        
        head = final[0]
        ptr = head
        for node in final[1:]:
            ptr.next = node
            ptr = ptr.next

        return head



        
