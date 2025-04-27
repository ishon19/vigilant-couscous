class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        
        current = "1"

        for _ in range(2, n+1):
            count = 1
            next_term = ""

            for i in range(1, len(current)):
                if current[i-1] == current[i]:
                    count += 1
                else:
                    next_term += str(count) + current[i-1]
                    count = 1
            
            next_term += str(count) + current[-1]
            current = next_term 
        
        return current 