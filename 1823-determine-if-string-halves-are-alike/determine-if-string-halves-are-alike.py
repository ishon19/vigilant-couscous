class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        a, b = s[:n//2], s[n//2:]
        print(a,b)
        h1, h2 = {}, {}

        for c in a:
            if c in vowels:
                if c not in h1:
                    h1[c] = 1
                else:
                    h1[c] += 1
        
        for c in b:
            if c in vowels:
                if c not in h2:
                    h2[c] = 1
                else:
                    h2[c] += 1
        print(h1, h2)
        return sum(list(h1.values())) == sum(list(h2.values()))
        


