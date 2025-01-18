class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        note = Counter(ransomNote)
        source = Counter(magazine)

        for char, count in note.items():
            if char not in source:
                return False
            if count > source[char]:
                return False
        
        return True