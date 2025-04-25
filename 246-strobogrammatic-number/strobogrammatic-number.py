class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        pairs = {'8': '8', '1':'1', '6':'9', '9':'6', '0': '0'}

        formation = ''
        for digit in num:
            if digit not in pairs:
                return False
            formation += pairs[digit]
        
        return formation[::-1] == num