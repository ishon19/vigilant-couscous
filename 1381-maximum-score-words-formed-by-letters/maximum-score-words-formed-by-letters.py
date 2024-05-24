class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        # Helper function to calculate score of a word
        def calculate_score(word):
            return sum(score[ord(ch) - ord('a')] for ch in word)
        
        # Backtracking function to find the maximum score
        def backtrack(index, current_count):
            if index == len(words):
                return 0
            
            max_score = 0
            word = words[index]
            word_count = Counter(word)
            
            # Check if the word can be formed with the remaining letters
            if all(current_count[char] >= word_count[char] for char in word_count):
                # Include the word
                for char in word_count:
                    current_count[char] -= word_count[char]
                max_score = calculate_score(word) + backtrack(index + 1, current_count)
                # Backtrack
                for char in word_count:
                    current_count[char] += word_count[char]
            
            # Exclude the word
            max_score = max(max_score, backtrack(index + 1, current_count))
            
            return max_score
        
        # Convert letters to a counter
        letter_count = Counter(letters)
        
        return backtrack(0, letter_count)