# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        s = 0
        ptr = head
        while ptr:
            s += 1
            ptr = ptr.next
        
        if s == n:
            head = head.next
            return head
        
        ptr = head
        i = 0
        while ptr:
            if i == s - n - 1:
                ptr.next = ptr.next.next
                break
            i += 1
            ptr = ptr.next
        
        return head
