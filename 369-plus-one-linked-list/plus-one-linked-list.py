# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        nums = []

        ptr = head
        while ptr:
            if not ptr.next:
                if ptr.val + 1 < 10:
                    ptr.val += 1
                    return head
            nums.append(str(ptr.val))
            ptr = ptr.next
        
        print('nums', nums)
        num = int(''.join(nums)) + 1
        newList = list(str(num))
        print('new list', newList)

        ptr = temp = head
        if len(nums) < len(list(str(num))):
             temp = ListNode(1, head)
             ptr = temp
        
        ptr2 = ptr
        for ele in newList:
            if ptr2:
                ptr2.val = ele
                ptr2 = ptr2.next
        
        print('final', ptr)
        
        return ptr

