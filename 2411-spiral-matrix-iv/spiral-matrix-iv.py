# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        values = []

        ptr = head
        while ptr:
            values.append(ptr.val)
            ptr = ptr.next
        
        res = [[-1] * n for _ in range(m)]

        top, bottom = 0, m - 1
        left, right = 0, n - 1
        idx = 0

        while top <= bottom and left <= right:
            # top row
            for i in range(left, right + 1):
                if idx < len(values): 
                    res[top][i] = values[idx]
                    idx += 1
            top += 1

            # right col
            for i in range(top, bottom + 1):
                if idx < len(values): 
                    res[i][right] = values[idx]
                    idx += 1
            right -= 1

            if not (top <= bottom and left <= right):
                break

            # bottom row
            for i in range(right, left - 1, -1):
                if idx < len(values): 
                    res[bottom][i] = values[idx]
                    idx += 1
            bottom -= 1
            
            # left col
            for i in range(bottom, top - 1, -1):
                if idx < len(values): 
                    res[i][left] = values[idx]
                    idx += 1
            left += 1
        
        return res