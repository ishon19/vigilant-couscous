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
        lists = [lst for lst in lists if lst]
        if not lists:
            return None

        heap = []
        for head in lists:
            heappush(heap, head)
        
        dummy = ListNode()
        curr = dummy
        while heap:
            head = heappop(heap)
            if head: 
                curr.next = head
                curr = curr.next
                head = head.next
                if head: 
                    heappush(heap, head)
        
        return dummy.next      
# @lc code=end

