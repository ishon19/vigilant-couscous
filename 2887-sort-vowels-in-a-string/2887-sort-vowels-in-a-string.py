class Solution:
    def sortVowels(self, s: str) -> str:
        cons = []
        vow = []

        def isVowel(char):
            return ord(char) in [65, 69, 73, 79, 85, 97, 101, 105, 111, 117]

        for i, char in enumerate(s):
            if isVowel(char):
                vow.append([char, i])
            else:
                cons.append([char, i])
        
        # record the ordering 
        order = [v for k,v in vow]
        # sort the vowels 
        vow.sort()
        #restore the order
        for i, o in enumerate(order):
            vow[i][1] = o
        
        res = vow + cons
        res.sort(key=lambda e: e[1])

        ans = ''
        for k,v in res:
            ans += k

        return ans            

