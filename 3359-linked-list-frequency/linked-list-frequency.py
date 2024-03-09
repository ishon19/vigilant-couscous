# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def frequenciesOfElements(self, head: Optional[ListNode]) -> Optional[ListNode]:
        counts = collections.defaultdict(int)

        while head:
            counts[head.val] += 1
            head = head.next
        
        # print('counts', counts)
    
        newHead = ListNode(-1)
        ptr = newHead

        for k, v in counts.items():
            newHead.next = ListNode(v)
            newHead = newHead.next
        
        return ptr.next

            