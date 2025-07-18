"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        node = Node(insertVal)

        if not head:
            node.next = node
            return node
        
        cur = head
        while True:
            if cur.val <= insertVal <= cur.next.val:
                break 
            
            if cur.val > cur.next.val:
                if insertVal > cur.val or insertVal < cur.next.val:
                    break 
            
            cur = cur.next

            if cur == head:
                break 
        
        node.next = cur.next
        cur.next = node

        return head 