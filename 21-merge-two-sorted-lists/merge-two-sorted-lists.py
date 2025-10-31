# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        save = dummy

        ptr1 = list1
        ptr2 = list2

        while ptr1 and ptr2:
            if ptr1.val < ptr2.val:
                dummy.next = ptr1
                ptr1 = ptr1.next
            else:
                dummy.next = ptr2
                ptr2 = ptr2.next
            dummy = dummy.next
        
        if ptr1:
            dummy.next = ptr1
        if ptr2:
            dummy.next = ptr2
        
        return save.next