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

        dummy = head
        ptr = head.next
        while ptr != head:
            if head.val < insertVal < ptr.val:
                save = head.next
                head.next = Node(insertVal)
                head.next.next = save
            else:
                save = ptr.next
                ptr.next = Node(insertVal)
                ptr.next.next = save
            ptr = ptr.next

        return dummy
# @lc code=end
