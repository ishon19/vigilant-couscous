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
        # the main challenge is to point to the non existant node to random        
        # start off by creating a hashmap to
        linkedhash = {None: None}
        
        curr = head
        while curr:
            copy = Node(curr.val)
            linkedhash[curr] = copy
            curr = curr.next
        
        curr = head
        while curr:
            copy = linkedhash[curr]
            copy.next = linkedhash[curr.next]
            copy.random = linkedhash[curr.random]
            curr = curr.next
        
        return linkedhash[head]