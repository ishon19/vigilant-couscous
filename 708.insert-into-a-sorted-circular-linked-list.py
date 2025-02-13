#
# @lc app=leetcode id=708 lang=python3
#
# [708] Insert into a Sorted Circular Linked List
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        newNode = Node(insertVal)

        if not head:
            newNode.next = newNode
            return newNode

        curr = head
        while True:
            if curr.val <= insertVal <= curr.next.val:
                break

            if curr.val > curr.next.val and (insertVal >= curr.val or insertVal <= curr.next.val):
                break

            if curr.next == head:
                break

            curr = curr.next
        
        newNode.next = curr.next
        curr.next = newNode
        return head
# @lc code=end

