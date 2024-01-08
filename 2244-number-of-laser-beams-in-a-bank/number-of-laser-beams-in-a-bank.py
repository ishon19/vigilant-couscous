class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        if len(bank) == 1:
            return 0
        
        res = 0
        prev = 0

        for row in bank:
            count = 0
            for cell in row:
                if cell == '1':
                    count += 1
            
            if count:
                res += count * prev
                prev = count
        
        return res