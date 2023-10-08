class Solution:
    def reverseWords(self, s: str) -> str:
        words = re.split(r'[^\S]+', s)
        print(words)
        return ' '.join([word[::-1] for word in words])