#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getKthNode(self, current, k):
        while current and k > 0:
            current = current.next
            k -= 1
        return current

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head

        dummy = ListNode(0, head)

        group_prev = dummy
        while True:
            kthNode = self.getKthNode(group_prev, k)
            if not kthNode:
                break

            start = kthNode.next
            prev = start
            curr = group_prev.next
            while curr != start:
                save = curr.next
                curr.next = prev
                prev = curr
                curr = save
            
            temp = group_prev.next
            group_prev.next = kthNode
            group_prev = temp
        
        return dummy.next

# @lc code=end

