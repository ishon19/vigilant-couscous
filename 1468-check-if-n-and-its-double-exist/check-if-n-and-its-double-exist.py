class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        evens, odds = [], []
        z_count = 0

        for num in arr:
            if num == 0: 
                z_count += 1
            elif num % 2 == 0:
                evens.append(num)
            else:
                odds.append(num)
        
        if z_count > 1:
            return True

        if not evens:
            return False
        
        for even in evens:
            if even//2 in arr:
                return True
        
        return False

