"""
CTCI 2.1: Remove Dups - Write code to remove duplicates from an unsorted linked list.
FOLLOW UP: How would you solve this problem if a temporary buffer is not allowed?

Example:
Input: 1 -> 2 -> 3 -> 3 -> 4 -> 5 -> 5 -> 5 -> 6
Output: 1 -> 2 -> 3 -> 4 -> 5 -> 6
"""
import collections

def removeDups(head):
    """
    Time: O(N)
    Space: O(N)
    """
    cnt = collections.Counter()
    cur = head
    while cur:
        cnt[cur.val] += 1
        cur = cur.next
    dummy = ListNode(0, head)
    pre, cur = dummy, head
    while cur:
        if cnt[cur.val] > 1:
            pre.next = cur.next
        else:
            pre = cur
        cur = cur.next
    return dummy.next