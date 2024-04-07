class Solution:
    def checkValidString(self, s: str) -> bool:
        memo = {}

        def helper(net, idx):
            if idx == len(s):
                return net == 0
            
            if (net, idx) in memo:
                return memo[(net, idx)]
            
            valid = False
            if s[idx] == '*':
                valid |= helper(net + 1, idx + 1)

                if net > 0:
                    valid |= helper(net - 1, idx + 1)
                valid |= helper(net, idx + 1)
            else:
                if s[idx] == '(':
                    valid = helper(net + 1, idx + 1)
                elif net > 0:
                    valid |= helper(net - 1, idx + 1)
            
            memo[(net, idx)] = valid
            return valid
        
        return helper(0, 0)

            

