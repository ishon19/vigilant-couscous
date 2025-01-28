# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0        
        output = ListNode()   
        ans = output
        while l1 or l2:
            nodeSum = carry + (l1.val if l1 else 0) + (l2.val if l2 else 0)
            carry = nodeSum//10         
            nodeVal = nodeSum%10
            newNode = ListNode(nodeVal, None)            
            output.next = newNode            
            if l1: l1 = l1.next
            if l2: l2 = l2.next  
            output = output.next
        if carry!=0:
            output.next = ListNode(carry,None)
        return ans.next
            