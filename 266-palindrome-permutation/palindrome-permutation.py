class Solution:
    def canPermutePalindrome(self, string: str) -> bool:
        if not string:
            return False
    
        # clean the string
        string = "".join(re.split('\W+', string.strip().lower()))
        # print(string)

        # map the characters
        counter = collections.Counter(string)
        # print(counter)
            
        
        # if there is just one key, it a palindrome
        if len(counter.keys()) == 1:
            return True
        else:
            # if all even its a palindrome
            allEven = True
            for k, v in counter.items():
                if v % 2 != 0:
                    allEven = False
                    break
            
            if allEven:
                return True
            
            # if all even but one odd, palindrome
            oddCount = 0
            for k, v in counter.items():
                if v % 2 != 0:
                    oddCount += 1
            
            if oddCount == 1:
                return True
        
        return False