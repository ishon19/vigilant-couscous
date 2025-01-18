class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        nums = re.findall(r'(\d+)', abbr)
        letters = re.findall(r'([a-z]+)', abbr)
        count1 = 0
        count2 = 0
        for num in nums:
            if num.startswith('0'):
                return False
            count1 += int(num)
        for letter in letters:
            if letter not in word:
                return False
                
            count2 += len(letter)
        return count1 + count2 == len(word)

        



        