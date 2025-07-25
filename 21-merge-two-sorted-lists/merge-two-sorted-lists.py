# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1, p2 = list1, list2
        finalList = ListNode()
        curr = finalList

        while p1 and p2:
            p1_val = p1.val if p1 else 0
            p2_val = p2.val if p2 else 0

            if p1_val < p2_val:
                curr.next = p1
                curr = curr.next
                p1 = p1.next
            else:
                curr.next = p2
                curr = curr.next
                p2 = p2.next
        
        curr.next = p1 if p1 else p2
        
        return finalList.next
            
        