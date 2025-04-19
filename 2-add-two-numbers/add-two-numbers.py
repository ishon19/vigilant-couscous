# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sumNode = ListNode()
        ptr = sumNode   
        carry = 0
        
        while l1 or l2 or carry:
            val = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry 
            carry = val // 10
            ptr.next = ListNode(val % 10)
            ptr = ptr.next 
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        
        return sumNode.next