# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # if list1 is None:
            # return list2
        # elif list2 is None:
            # return list1
        
        # if list1.val < list2.val:
            # list1.next = self.mergeTwoLists(list1.next, list2)
            # return list1
        # else:
            # list2.next = self.mergeTwoLists(list1, list2.next)            
            # return list2
        
        # Iterative solution
        dummy = ListNode()
        tail = dummy
        
        while l1 and l2:
            if l1.val<l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        
        if l1:
            tail.next = l1
        else:
            tail.next = l2
        
        return dummy.next