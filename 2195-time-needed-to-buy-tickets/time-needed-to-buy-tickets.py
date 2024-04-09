class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        res = 0

        while tickets[k]>0:
            for i, ticket in enumerate(tickets):
                if tickets[i] != 0:
                    tickets[i] -= 1
                    res += 1
            
                if tickets[k] == 0:
                    break
 
        return res