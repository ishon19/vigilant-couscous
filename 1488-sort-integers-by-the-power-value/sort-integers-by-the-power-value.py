class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        def getSteps(x):
            count = 0
            while x != 1:
                if x % 2 == 0:
                    x = x // 2
                else:
                    x = ((3 * x) + 1)
                count += 1
            return count
        
        powers = [(getSteps(num), num) for num in range(lo, hi+1)]
        heapify(powers)
        
        while k - 1:
            heappop(powers)
            k -= 1
            
        return powers[0][1]