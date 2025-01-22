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
        linkMap = defaultdict(Node)
        linkMap[None] = None

        ptr = head
        while ptr:
            linkMap[ptr].val = ptr.val
            linkMap[ptr].next = 
# @lc code=end

