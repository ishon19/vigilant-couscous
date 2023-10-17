# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        ptr = head
        temp = []
        while ptr:
            temp.append(str(ptr.val))
            ptr = ptr.next
        string = ''.join(temp)
        # print(string)
        return string == string[::-1]