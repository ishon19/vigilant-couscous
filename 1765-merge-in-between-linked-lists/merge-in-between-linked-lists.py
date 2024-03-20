# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        prev_a_node = None
        next_b_node = None

        dummy = ListNode(-1, list1)

        # find the nodes
        ptr = list1
        count = 0
        while ptr:
            if count == a - 1:
                prev_a_node = ptr
            elif count == b:
                next_b_node = ptr
            ptr = ptr.next
            count += 1
        
        # stitch the second node
        prev_a_node.next = list2
        
        ptr = list2
        while ptr.next:
            ptr = ptr.next

        ptr.next = next_b_node.next

        return dummy.next
