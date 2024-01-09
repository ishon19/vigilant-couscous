class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        counter = collections.Counter(s)
        print(counter)
        
        # check if the answer is possible
        allEven = False
        for k,v in counter.items():
            if v % 2 == 0: 
                allEven = True
        
        if not allEven: 
            print('early break')
            return -1
    
        res = 0
        for k,v in counter.items():
            # find the first occurance in the normal string
            idx1 = s.index(k)
            idx2 = s[::-1].index(k)
            print(s, idx1, len(s)-1-idx2)
            res = max(res, len(s)-1-idx2 - idx1 - 1)
        return res

