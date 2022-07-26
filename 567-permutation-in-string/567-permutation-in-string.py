class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # base case, if the length of the string we are looking for is greater
        # than the length of the parent string return false right away
        if len(s1) > len(s2):
            return False
        
        # variants of hashmap, since the values are english alphabets, we can
        # use array for this purpose
        c1, c2 = [0] * 26, [0] * 26
        
        # assign the values in the array above based on the presence of
        # characters in the s1 string, along the way also update the s2
        # string
        for i in range(len(s1)):
            c1[ord(s1[i]) - ord('a')] += 1
            c2[ord(s2[i]) - ord('a')] += 1
        
        # count all the matches
        matches = 0
        for i in range(26):
            if c1[i] == c2[i]: matches += 1
        
        # sliding window
        l = 0
        # start off from the point where we calculated the counts previously
        # and the counts for s2 are still pending
        for r in range(len(s1), len(s2)):
            # if before reaching this point, we already have the counts as 26 
            # means we are good to go and the permutation matched based on the counts
            if matches == 26: return True
            
            # otherwise, carry on and this index below can be any, based on the ascii code
            idx = ord(s2[r]) - ord('a')
            c2[idx] += 1
            
            # if by any chance by doing above, we match the same index in the s1 string as well
            # then increase the matches else decrease the matches
            if c1[idx] == c2[idx]: matches += 1
            elif c1[idx] + 1 == c2[idx]: matches -= 1
            
            # removing a character with the left pointer
            idx = ord(s2[l]) - ord('a')
            # just removed, so decrement the count
            c2[idx] -= 1
            if c1[idx] == c2[idx]: matches += 1
            elif c1[idx] - 1 == c2[idx]: matches -= 1
            l += 1
        
        return matches == 26
            
            
            
        