class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])
        count = 0
        last = float("-inf")

        for pair in pairs:
            if pair[0] > last:
                count += 1
                last = pair[1]
        
        return count
