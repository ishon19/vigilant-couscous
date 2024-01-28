class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        res = letters[0]
        for char in letters:
            if ord(char) > ord(target):
                return char
        return res