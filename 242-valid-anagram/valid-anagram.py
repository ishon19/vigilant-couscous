class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_s = sorted([[k,v] for k,v in Counter(s).items()], key=lambda x: (x[1],x[0]))
        freq_t = sorted([[k,v] for k,v in Counter(t).items()], key=lambda x: (x[1],x[0]))
        return freq_s == freq_t