# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def gameResult(self, head: Optional[ListNode]) -> str:
        even, odd = 0, 0

        ptr = head
        while ptr:
            # print(ptr.val, ptr.next.val)
            if ptr.val > ptr.next.val:
                even += 1
            else:
                odd += 1
            ptr = ptr.next.next

        return "Tie" if even == odd else "Even" if even > odd else "Odd"