class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        stack = []

        for word in words:
            if stack and len(stack) >= 1:
                if Counter(word) == Counter(stack[-1]):
                    continue
            stack.append(word)
        
        return stack 