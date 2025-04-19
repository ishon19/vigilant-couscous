#
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        nodeMap = {}

        curr = head
        while curr:
            nodeMap[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            if curr.next:
                nodeMap[curr].next = nodeMap[curr.next]
            
            if curr.random:
                nodeMap[curr].random = nodeMap[curr.random]
            
            curr = curr.next
        
        return nodeMap[head]
               
# @lc code=end

