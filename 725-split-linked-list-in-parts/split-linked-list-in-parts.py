# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
10, 3

10/3 = 3
remains = 1

"""

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        res = [None] * k

        size = 0
        cur = head
        while cur:
            size += 1
            cur = cur.next
        
        splits = size // k
        excess = size % k

        cur = head
        for i in range(k):
            new_part = ListNode(0)
            tail = new_part

            cur_size = splits
            if excess > 0:
                excess -= 1
                cur_size += 1
            for j in range(cur_size):
                tail.next = ListNode(cur.val)
                tail = tail.next
                cur = cur.next
            res[i] = new_part.next
        
        return res