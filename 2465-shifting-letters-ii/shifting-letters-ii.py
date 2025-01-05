class Solution:
    def shift(self, letter, times):
        return chr((ord(letter) - ord('a') + times) % 26 + ord('a')) 

    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        finalShifts = [0] * len(s)

        for start, end, direction in shifts:
            delta = 1 if direction == 1 else -1
            finalShifts[start] += delta
            if end + 1 < len(s):
                finalShifts[end + 1] -= delta

        for i in range(1, len(s)):
            finalShifts[i] += finalShifts[i - 1]
        
        res = ''
        for i, shift in enumerate(finalShifts):
            res += self.shift(s[i], shift)
        
        return res