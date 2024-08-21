class Solution:
    def nthUglyNumber(self, n: int) -> int:
        numset = set([1])
        current_ugly = 1

        for i in range(n):
            current_ugly = min(numset)
            numset.remove(current_ugly)

            numset.add(current_ugly * 2)
            numset.add(current_ugly * 3)
            numset.add(current_ugly * 5)
        
        return current_ugly
        

            
