# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        
        cur_head = head
        next_head = head.next
        
        cur_head.next = self.swapPairs(next_head.next)
        next_head.next = cur_head
        
        return next_head
        