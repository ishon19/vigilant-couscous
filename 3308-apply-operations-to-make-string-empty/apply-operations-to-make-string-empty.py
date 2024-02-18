class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        hm = {}

        for idx, char in enumerate(s):
            if char in hm:
                hm[char].append(idx)
            else:
                hm[char] = [idx]
        
        maxFreq = max(len(count) for count in hm.values())

        lastIdxes = []
        for k, v in hm.items():
            if len(v) != maxFreq:
                continue
            else:
                lastIdxes.append([k, v[-1]])
        
        lastIdxes.sort(key=lambda x: x[1])
        res = ''
        for ele in lastIdxes:
            res += ele[0]
        
        return res
