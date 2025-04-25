#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        finalList = ListNode()
        ptr1, ptr2, ptr3 = l1, l2, finalList
        carry = 0

        while ptr1 or ptr2 or carry:
            current_sum = (ptr1.val if ptr1 else 0) + \
                (ptr2.val if ptr2 else 0) + carry
            ptr3.next = ListNode(current_sum % 10)
            carry = current_sum // 10
            ptr1 = ptr1.next if ptr1 else None
            ptr2 = ptr2.next if ptr2 else None
            ptr3 = ptr3.next

        return finalList.next
# @lc code=end
