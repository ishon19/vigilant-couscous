#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2

        if not list2:
            return list1
        
        newList = ListNode(-1)
        dummy = newList

        ptr1, ptr2 = list1, list2

        while ptr1 and ptr2:
            if ptr1.val < ptr2.val:
                newList.next = ptr1
                ptr1 = ptr1.next
            else:
                newList.next = ptr2
                ptr2 = ptr2.next
            newList = newList.next
        
        if ptr1:
            newList.next = ptr1
        else:
            newList.next = ptr2
        
        return dummy.next
        
# @lc code=end

