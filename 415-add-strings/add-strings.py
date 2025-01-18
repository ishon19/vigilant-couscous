class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        buf = []
        carry = 0
        p1, p2 = len(num1) - 1, len(num2) - 1

        while p1>=0 or p2>=0 or carry:
            total = int(num1[p1] if p1>=0 and num1[p1].isdigit() else 0) + int(num2[p2] if p2>=0 and num2[p2].isdigit() else 0) + carry
            buf.append(str(total % 10))
            carry = total // 10
            p1 -= 1
            p2 -= 1
        
        return "".join(buf)[::-1] if buf else "0"
        

