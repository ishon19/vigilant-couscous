class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        counter = collections.Counter(s)

        if '1' not in counter:
            return '0' * len(counter.keys())
        else:
            onesCount = counter['1']

            if onesCount == 1:
                return ('0' * counter['0']) + '1'
            else:
                res = ''
                while counter['1'] > 1:
                    res += '1'
                    counter['1'] -= 1
                
                while counter['0']:
                    res += '0'
                    counter['0'] -= 1
                
                res += '1'
                return res
