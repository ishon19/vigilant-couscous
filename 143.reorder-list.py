#
# @lc app=leetcode id=143 lang=python3
#
# [143] Reorder List
#
# None<-0<-1 2
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        prev = None
        ptr = head

        while ptr:
            save = ptr.next
            ptr.next = prev
            prev = ptr
            ptr = save
        
        return prev
    
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # use fast and slow pointers to reach till the middle of the list
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # slow should be at the middle now, reverse it
        first, second = head, self.reverseList(slow)

        while second.next:
            saveFirst = first.next
            saveSecond = second.next

            first.next = second
            second.next = saveFirst

            first = saveFirst
            second = saveSecond
        

# @lc code=end

