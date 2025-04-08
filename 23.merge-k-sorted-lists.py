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
        heap = []

        for i, list in enumerate(lists):
            if list:
                heappush(heap, (list.val, i, list))
        
        dummyNode = ListNode()
        ptr = dummyNode
        while heap:
            _, idx, list = heappop(heap)
            ptr.next = list
            if list.next:
                heappush(heap, (list.next.val, idx, list.next))
            ptr = ptr.next

        return dummyNode.next
# @lc code=end

