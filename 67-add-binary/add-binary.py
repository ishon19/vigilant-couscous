class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if not a and not b:
            return ""        
        if not a:
            return b        
        if not b:
            return a
        
        if len(a) > len(b):
            b =  "0" * (len(a) - len(b)) + b
        else:
            a = "0" * (len(b) - len(a)) + a
        
        carry = 0
        a = a[::-1]
        b = b[::-1]
        res = ""
        for i in range(len(a)):
            if a[i] == '0' and b[i] == '0':
                res += '1' if carry else '0'
                carry = 0
            elif (a[i] == '1' and b[i] == '0') or (a[i] == '0' and b[i] == '1'):
                res += '1' if not carry else '0'
                carry = 1 if carry else 0
            elif a[i] == '1' and b[i] == '1':
                if carry:
                    res += "1"
                else:
                    res += "0"
                carry += 1
        if carry:
            res += "1"
        return res[::-1]