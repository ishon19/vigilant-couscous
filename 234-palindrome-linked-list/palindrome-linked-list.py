# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # O(n) way
        # ptr = head
        # temp = []
        # while ptr:
        #     temp.append(str(ptr.val))
        #     ptr = ptr.next
        # string = ''.join(temp)
        # # print(string)
        # return string == string[::-1]

        # constant space way
        if not head:
            return True
        
        first_half_end = self.mid_list(head)
        second_half_start = self.reverse_list(first_half_end.next)
        
        res = True
        first = head
        second = second_half_start
        while res and second:
            if first.val != second.val: 
                res = False
            first = first.next
            second = second.next
        
        first_half_end.next = self.reverse_list(second_half_start)
        return res
    
    def mid_list(self, head):
        fast = head
        slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        return slow

    def reverse_list(self, head):
        ptr = head
        prev = None
        while ptr:
            ptr_next = ptr.next
            ptr.next = prev
            prev = ptr
            ptr = ptr_next
        return prev