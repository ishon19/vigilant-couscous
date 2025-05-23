class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        res = []
        sentenceList = sentence.split(" ")

        for i, word in enumerate(sentenceList):
            if word[0].lower() in 'aeiou':
                res.append(word + 'ma' + 'a' * (i+1))
            else:
                res.append(word[1:]+word[0]+'ma' + 'a' * (i+1))
 
        return ' '.join(res)