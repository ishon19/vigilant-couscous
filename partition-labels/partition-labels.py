class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # track the last index of each character
        # and the index with the max last encountered
        # on a running basis is the end of a partition
        res = []
        char_last_occurance = {char: i for i, char in enumerate(s)}
        start = 0
        end = 0
        
        for i in range(len(s)):
            end = max(end, char_last_occurance[s[i]])
            if i == end:
                res.append(end-start+1)
                start = i + 1
        
        return res
    