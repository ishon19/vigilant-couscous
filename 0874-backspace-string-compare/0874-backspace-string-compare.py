class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = []
        stack2 = []

        for c in s:
            if stack1:
                if c == '#': stack1.pop()
                else: stack1.append(c)
            else: 
                if c!= '#': stack1.append(c)
        
        for c in t:
            if stack2:
                if c == '#': stack2.pop()
                else: stack2.append(c)
            else:
                if c!= '#': stack2.append(c)

        print(stack1, stack2)

        return stack1 == stack2