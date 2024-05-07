# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # brute force solution
        # nums = []
        # ptr = head
        # while ptr:
        #     nums.append(str(ptr.val))
        #     ptr = ptr.next
        # num = int(''.join(nums))
        # double = list(str(num * 2))
        # # print(double)
        # head = ListNode(int(double[0]))
        # ptr = head
        # for num in double[1:]:
        #     ptr.next = ListNode(int(num))
        #     ptr = ptr.next
        # return head

        def revList(node):
            if not node or not node.next:
                return node
            newNode = revList(node.next)
            node.next.next = node
            node.next = None
            return newNode

        carry = 0
        revlist = revList(head)
        ptr = revlist

        while ptr:
            curval = ptr.val * 2 
            if curval >= 10:
                ptr.val = curval % 10
                if carry: ptr.val += carry
                carry = 1
            else:
                ptr.val = curval + carry
                carry = 0
            
            if ptr.next == None and carry:
                ptr.next = ListNode(1)
                ptr = ptr.next
            
            ptr = ptr.next

        head = revList(revlist)
        
        return head