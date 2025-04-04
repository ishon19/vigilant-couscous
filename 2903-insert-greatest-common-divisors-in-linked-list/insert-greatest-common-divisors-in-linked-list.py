# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode(-1, head)
        ptr = head
        while ptr.next:
            ptr.next = ListNode(math.gcd(ptr.val,  ptr.next.val), ptr.next)
            ptr = ptr.next.next
        return temp.next