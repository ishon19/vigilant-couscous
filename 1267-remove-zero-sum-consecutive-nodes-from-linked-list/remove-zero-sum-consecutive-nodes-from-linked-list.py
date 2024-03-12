# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if not head or not head.next:
        #     return None
            
        # stack = []

        # while head:
        #     if stack:
        #         if stack[-1].val + head.val == 0:
        #             stack.pop()
        #         else:
        #             stack.append(head)
        #     else:
        #         stack.append(head)
        #     head = head.next
        
        # if not stack:
        #     return None
        
        # newList = ListNode(stack[0].val)
        # newHead = newList

        # for node in stack[1:]:
        #     newList.next = ListNode(node.val)
        #     newList = newList.next
        
        # return newHead

        front = ListNode(0, head)
        start = front

        while start:
            pref = 0
            end = start.next

            while end:
                pref += end.val
                if pref == 0:
                    start.next = end.next
                end = end.next
            start = start.next
        
        return front.next
        