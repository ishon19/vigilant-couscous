#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ListNode.__lt__ = lambda self, other: self.val < other.val

        heap = []

        for head in lists:
            if head:
                heappush(heap, head)
            
        dummy = ListNode(0)
        curr = dummy

        while heap:
            node = heappop(heap)
            curr.next = node
            curr = curr.next
        
            if node.next:
                heappush(heap, node.next)

        return dummy.next
# @lc code=end

