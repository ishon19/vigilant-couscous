class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # plus one for the base case
        dp = [None] * (len(s)+1)
        dp[len(s)] = True
        for i in reversed(range(len(s))):
            for word in wordDict:
                # if within the bounds and the string matches word
                if i + len(word) <= len(s) and s[i: i + len(word)] == word:
                    dp[i] = dp[i+len(word)]
                # else, if dp[i] is already set then we can break from the loop
                if dp[i]:
                    break
        return dp[0]