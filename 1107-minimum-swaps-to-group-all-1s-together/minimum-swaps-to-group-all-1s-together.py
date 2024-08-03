class Solution:
    def minSwaps(self, data: List[int]) -> int:
         totalOnes = data.count(1)
         l, r = 0, 0 
         curOnes = 0
         maxOnes = 0

         while r < len(data):
            curOnes += data[r]

            if r - l + 1 > totalOnes:
                curOnes -= data[l]
                l += 1
            
            if r - l + 1 == totalOnes:
                maxOnes = max(maxOnes, curOnes)
            
            r += 1
        
         return totalOnes - maxOnes