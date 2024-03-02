# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
            
        def mergeTwoLists(list1, list2):
            if not list1 and not list2:
                return None
            
            if list1 and not list2:
                return list1
            
            if list2 and not list1:
                return list2
            
            if list1.val < list2.val:
                list1.next = mergeTwoLists(list1.next, list2)
                return list1
            else:
                list2.next = mergeTwoLists(list1, list2.next)
                return list2
        
        head = lists[0]
        for i in range(len(lists) - 1):
            mergedList = mergeTwoLists(head, lists[i+1])
            head = mergedList
        
        return head
        


            