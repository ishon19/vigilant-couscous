class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}

        def helper(i, j):
            if (i,j) in memo:
                return memo[(i,j)]
            
            if i == 0:
                return j
            
            if j ==0:
                return i
            
            if word1[i-1] == word2[j-1]:
                memo[(i,j)] = helper(i-1, j-1)
            else:
                memo[(i,j)] = 1 + min(helper(i-1, j), helper(i, j-1), helper(i-1, j-1))
            
            return memo[(i,j)]
        
        return helper(len(word1), len(word2))