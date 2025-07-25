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
        copy_cache = {None:None}

        ptr = head 
        while ptr:
            if ptr not in copy_cache:
                copy = Node(ptr.val)
                copy_cache[ptr] = copy
                ptr = ptr.next

        ptr = head 
        while ptr:
            node = copy_cache[ptr]
            node.next = copy_cache[ptr.next]
            node.random = copy_cache[ptr.random]
            ptr = ptr.next

        return copy_cache[head] 