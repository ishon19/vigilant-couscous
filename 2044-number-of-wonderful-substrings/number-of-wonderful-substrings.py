class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        # create hashmap of bitmask and freq
        freq = {}

        freq[0] = 1

        mask = 0
        res = 0
        for c in word:
            bit = ord(c) - 97
            mask ^= (1 << bit)

            if mask in freq:
                res += freq[mask]
                freq[mask] += 1
            else:
                freq[mask] = 1
            
            for odd_c in range(10):
                if (mask ^ (1 << odd_c)) in freq:
                    res += freq[mask ^ (1 << odd_c)]
        
        return res
