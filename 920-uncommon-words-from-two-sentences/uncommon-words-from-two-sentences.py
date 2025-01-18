"""

s1 = "this apple is sweet"
s2 = "this apple is sour"

res = [sweet, sour]

h1 = {this: 1, apple: 1, is: 1, sweet: 1}
res = [sour]
h2 = {}


"""
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        c1 = collections.Counter(s1.split())
        c2 = collections.Counter(s2.split())
        res = []
        for char1 in c1.keys():
            if c1[char1] ==1 and char1 not in c2.keys():
                res.append(char1)
        for char2 in c2.keys():
            if c2[char2] == 1 and char2 not in c1.keys():
                res.append(char2)
        
        return res
        
        