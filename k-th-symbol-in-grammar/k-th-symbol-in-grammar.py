class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        # draw the tree to get a better visualization
        # based on whether the value of k is even or odd
        if k%2 == 0:
            # left side of node
            return 1 if self.kthGrammar(n-1, math.floor(k/2)) == 0 else 0
        else:
            return 0 if self.kthGrammar(n-1, math.floor((k+1)/2)) == 0 else 1
            
            