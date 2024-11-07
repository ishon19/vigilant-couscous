class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        # we need to check if the same bit in every candidate
        # has a set bit and the max count of any such bit would
        # give us the answer
        
        # so how many bits can a number have?
        # easy, check the constraints (10^5 < 2^24) 
        # so going over 24 bits is just fine

        # array to keep counts of bits at a particular position
        bit_count = [0] * 24
        for i in range(24):
            for candidate in candidates:
                if candidate & (1 << i) != 0:
                    bit_count[i] += 1
        
        return max(bit_count)