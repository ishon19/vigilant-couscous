# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        start = None
        end = None

        n = 0
        ptr = head
        while ptr:
            n += 1
            if n == k: start = ptr
            ptr = ptr.next
        
        # print('size of the list is', n)
        # print('start', start)

        ptr = head
        i = 1
        while ptr:
            if i == n - k + 1:
                start.val, ptr.val = ptr.val, start.val
                break
            i += 1
            ptr = ptr.next

        return head