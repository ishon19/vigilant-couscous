# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None
        rev_second = self.reverse_list(second)
        # print('rev', rev_second)

        first, second = head, rev_second        
        while second:
            t1, t2 = first.next, second.next
            first.next = second
            second.next = t1
            first, second = t1, t2
    
    def reverse_list(self, head):
        if not head:
            return None
        
        ptr = head
        prev = None
        while ptr:
            ptr_next = ptr.next
            ptr.next = prev
            prev = ptr
            ptr = ptr_next
        return prev
        
        