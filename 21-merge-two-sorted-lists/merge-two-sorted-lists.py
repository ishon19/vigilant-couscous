# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 29 Nov 2024, 2.45 AM attempt
        if not list1 and not list2:
            return None
        
        if not list1 or not list2:
            return list1 if list1 is not None else list2
        
        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list2.next, list1)
            return list2
    
        """        
            if not list1 and not list2:
                return None
            
            if list1 and not list2:
                return list1
            
            if list2 and not list1:
                return list2
            
            if list1.val < list2.val:
                list1.next = self.mergeTwoLists(list1.next, list2)
                return list1
            else:
                list2.next = self.mergeTwoLists(list1, list2.next)
                return list2
            """