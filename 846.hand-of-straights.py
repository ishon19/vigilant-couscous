#
# @lc app=leetcode id=846 lang=python3
#
# [846] Hand of Straights
#

# @lc code=start
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # base case
        if len(hand) % groupSize != 0:
            return False
        
        cardCount = Counter(hand)
        sortedCards = sorted(cardCount.keys())

        for card in sortedCards:
            while cardCount[card] > 0:
                for i in range(groupSize):
                    if cardCount[card + i] <= 0:
                        return False
                    cardCount[card + i] -= 1
        
        return True

# @lc code=end

