class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        res = [0] * (len(num1) + len(num2))

        if not res:
            return "0"

        for i, n1 in enumerate(reversed(num1)):
            for j, n2 in enumerate(reversed(num2)):
                res[i+j] += int(n1) * int(n2)
                res[i+j+1] += res[i+j] // 10
                res[i+j] %= 10

        while res and res[-1] == 0:
            res.pop()

        return "".join(map(str, reversed(res))) 
        
        