"""
CTCI 2.3: Delete Middle Node - Implement an algorithm to delete a node in the middle (i.e. any node but the first and last node,
not necessarily the exact middle) of a singly linked list, given only access to that node.

Example:
Input: the node c from the linked list a -> b -> c -> d -> e -> f
Output: nothing is returned, but the new linked list looks like a -> b -> d -> e -> f
"""

# my solution
def delete_middle_node(node):
    """
    Time: O(1)
    Space: O(1)
    """
    if not node:
            return

    while node.next.next:
        node.val = node.next.val
        node = node.next
    
    node.val = node.next.val
    node.next = None

# CTCI solution
def delete_middle_node2(node):
    """
    Time: O(1)
    Space: O(1)
    """
    if not node or not node.next:
        return False
    
    node.val = node.next.val
    node.next = node.next.next
    return True