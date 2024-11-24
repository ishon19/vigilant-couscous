# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def get_list_center(self, head: Optional[ListNode]) -> ListNode:
        fast, slow = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def reverse_list(self, head: Optional[ListNode]) -> ListNode:
        prev = None
        ptr = head
        while ptr:
            next = ptr.next
            ptr.next = prev
            prev = ptr
            ptr = next
        return prev

    def pairSum(self, head: Optional[ListNode]) -> int:
        first_half_end = self.get_list_center(head)
        second_half_reversed = self.reverse_list(first_half_end)

        first, second = head, second_half_reversed
        max_sum = 0
        while first and second:
            max_sum = max(max_sum, first.val + second.val)
            first = first.next
            second = second.next
        
        # restore the original list
        first_half_end.next = self.reverse_list(second_half_reversed)
        return max_sum