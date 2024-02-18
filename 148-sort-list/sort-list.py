# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        order = []

        ptr = head
        while ptr:
            order.append(ptr.val)
            ptr = ptr.next
        
        order.sort()
        print(order)
        ptr = head
        i = 0
        while ptr:
            ptr.val = order[i]
            i += 1
            ptr = ptr.next
            
        return head