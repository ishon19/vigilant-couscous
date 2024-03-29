# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # prev = None
        # ptr = head
        # while ptr:
        #     ptr_next = ptr.next
        #     ptr.next = prev
        #     prev = ptr
        #     ptr = ptr_next        
        # return prev

        # recursive
        if not head or not head.next:
            return head
        
        temp = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return temp