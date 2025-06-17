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
        
        prev, curr = head, head.next
        while True:
            if prev.val <= insertVal <= curr.val:
                break 
            
            if prev.val > curr.val:
                if prev.val <= insertVal or curr.val >= insertVal:
                    break             

            prev, curr = curr, curr.next

            if prev == head:
                break 


        prev.next = newNode
        newNode.next = curr
        return head