class LinkedList:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        # inc = 0
        # for space in spaces:
        #     s = s[:space+inc] + " " + s[space+inc:]
        #     inc += 1
        # return s
        temp = ptr = charList = LinkedList('')

        for i in range(len(s)):
            charList.next = LinkedList(s[i])
            charList = charList.next
    
        res = ''
        ptr = ptr.next
        i = 0
        for space in spaces:
            while i != space:
                res += ptr.val
                ptr = ptr.next
                i += 1
            res += ' '
        
        while ptr:
            res += ptr.val
            ptr = ptr.next
        
        return res


