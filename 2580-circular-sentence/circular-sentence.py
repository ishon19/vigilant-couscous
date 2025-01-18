class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        if not sentence:
            return False 

        if sentence[0] != sentence[-1]:
            return False

        words = sentence.split(" ")
        
        for i in range(1, len(words)):
            if words[i-1][-1] != words[i][0]:
                return False
            
        return True



