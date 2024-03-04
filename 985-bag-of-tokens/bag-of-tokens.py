class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        score = 0
        tokens.sort()
        l, r = 0, len(tokens) - 1

        # while tokens:
            # minToken = min(tokens)
            # minTokenIdx = tokens.index(minToken)
            # maxToken = max(tokens)
            # maxTokenIdx = tokens.index(maxToken)
            # if score < 1:
            #     # can just play face up
            #     if minToken <= power:
            #         score += 1
            #         power -= minToken
            #         tokens.pop(minTokenIdx)
            #     else:
            #         break             
            # else:
            #     # can play either way                
            #     if len(tokens) <= 1:
            #         # play face up
            #         power -= minToken
            #         score += 1
            #         tokens.pop(minTokenIdx)
            #     else:
            #         # get rid of the most expensive one by buying it
            #         score -= 1
            #         power =+ maxToken
            #         tokens.pop(maxTokenIdx)
        while l <= r:
            # enough power, play face up
            if power >= tokens[l]:
                score += 1
                power -= tokens[l]
                l += 1
            elif l < r and score > 0:
                score -= 1
                power += tokens[r]
                r -= 1
            else:
                break

        return score


            
