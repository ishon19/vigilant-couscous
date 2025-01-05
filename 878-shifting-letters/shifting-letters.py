class Solution:
    def shift(self, letter, times):
        return chr((ord(letter) - ord('a') + times) % 26 + ord('a')) 

    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        prefix = [shifts[-1]]
        for i in reversed(range(len(shifts)-1)):
            prefix.append(prefix[-1] + shifts[i])
        prefix = prefix[::-1]

        res = ''
        for i, times in enumerate(prefix):
            shifted = self.shift(s[i], times)
            print(shifted)
            res += shifted
        return res