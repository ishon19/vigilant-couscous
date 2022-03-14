import re

class Solution:
    def freqAlphabets(self, s: str) -> str:
        d1 = {str(i-96): str(chr(i)) for i in range(97, 106)}
        d2 = {str(i-96): str(chr(i)) for i in range(106, 123)}

        # print(d1,'\n',d2)

        ans, i = '', 0
        while(i < len(s)):
            if((i+2) < len(s) and s[i+2] == '#'):
                ans += d2[str(s[i:i+2])]
                i += 3
            elif d1[str(s[i])]:
                ans += d1[str(s[i])]
                i += 1
                if i == len(s):
                    break
        return ans

    def freqAlphabets2(self, s: str) -> str:
        return ''.join(chr(int(i[:2]) + 96) for i in re.findall(r'\d\d#|\d', s))


if __name__ == '__main__':
    s = Solution()
    print(s.freqAlphabets("10#11#12"))  # "jkab"
    print(s.freqAlphabets("1326#"))  # "acz"
    print(s.freqAlphabets("10#11#12"))  # "jkab"
    print(s.freqAlphabets("1326#")) # "acz"
