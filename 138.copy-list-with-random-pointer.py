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
        # use hashmap based approach to store the links
        linkMap = {None: None}

        ptr = head
        while ptr:
            linkMap[ptr] = Node(ptr.val)
            ptr = ptr.next
        
        ptr = head
        while ptr:
            if ptr.next:
                linkMap[ptr].next = linkMap[ptr.next]
            if ptr.random:
                linkMap[ptr].random = linkMap[ptr.random]
            ptr = ptr.next
        
        return linkMap[head]

# @lc code=end

