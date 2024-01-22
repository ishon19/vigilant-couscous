"""
CTCI 2.2: Implement an algorithm to find the kth to last element of a singly linked list.

Example:
Input: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10, k = 3
Output: 8
"""

def kth_to_last(head, k):
    """
    Time: O(N)
    Space: O(1)
    """
    slow = fast = head
    for _ in range(k):
        fast = fast.next
    while fast:
        slow, fast = slow.next, fast.next
    return slow