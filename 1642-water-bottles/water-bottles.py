class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = numBottles

        while numBottles >= numExchange:
            exchanged = numBottles // numExchange
            excess = numBottles % numExchange
            res += exchanged
            numBottles = excess + exchanged          
            
        return res