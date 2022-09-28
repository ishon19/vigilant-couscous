# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        temp1 = dummy.next
        
        # move to distance 
        for _ in range(n):
            temp1 = temp1.next
        
        temp2 = dummy
        while temp1:
            temp1 = temp1.next
            temp2 = temp2.next                        
                
        temp2.next = temp2.next.next
        
        return dummy.next