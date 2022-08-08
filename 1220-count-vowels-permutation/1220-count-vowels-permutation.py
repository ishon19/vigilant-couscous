class Solution:
    def countVowelPermutation(self, n: int) -> int:    
        a, e, i, o, u = 1, 1, 1, 1, 1
        # figure out how many ways each character is generated in the next cycle
        # we start with 1, so if in next iteration we have some character how 
        # would it had been generated, if we draw the diagram it's easy to see
        for _ in range(n - 1):
            a, e, i, o, u = e + i + u, a + i, e + o, i, i + o
        return (a + e + i + o + u) % (10**9 + 7)