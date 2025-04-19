class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        last_op = "+"
        res = 0

        for i, char in enumerate(s):
            if char.isdigit():
                res = 10 * res + int(char)
            
            if char in "+-/*" or i == len(s) - 1:
                if last_op == "+":
                    stack.append(res)
                elif last_op == '-':
                    stack.append(-res)
                elif last_op == "*":
                    stack.append(stack.pop() * res)
                elif last_op == '/':
                    stack.append(int(stack.pop() / res))
                
                res = 0
                last_op = char
        
        return sum(stack)
