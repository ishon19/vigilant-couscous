# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode(0, head)
        nums = set(nums)
        ptr = temp
        while ptr:
            if ptr.next and ptr.next.val in nums:
                ptr.next = ptr.next.next
            else:
                ptr = ptr.next
        
        return temp.next


